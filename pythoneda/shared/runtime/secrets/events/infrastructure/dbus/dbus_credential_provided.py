# vim: set fileencoding=utf-8
"""
pythoneda/shared/runtime/secrets/events/infrastructure/dbus/dbus_credential_provided.py

This file defines the DbusCredentialProvided class.

Copyright (C) 2024-today rydnr's pythoneda-shared-runtime/secrets-events-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from dbus_next import BusType, Message
from dbus_next.service import ServiceInterface, signal
import json
from pythoneda.shared import BaseObject, Event
from pythoneda.runtime.secrets.events import CredentialProvided
from pythoneda.runtime.secrets.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusCredentialProvided(BaseObject, ServiceInterface):
    """
    D-Bus interface for CredentialProvided

    Class name: DbusCredentialProvided

    Responsibilities:
        - Define the d-bus interface for the CredentialProvided event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusCredentialProvided.
        """
        super().__init__("Pythoneda_Secrets_CredentialProvided")

    @signal()
    def CredentialProvided(self, name: "s", value: "s", metadata: "s"):
        """
        Defines the CredentialProvided d-bus signal.
        :param name: The credential name.
        :type name: str
        :param value: The credential.
        :type value: str
        :param metadata: The metadata.
        :type metadata: str
        """
        pass

    @property
    def path(self) -> str:
        """
        Retrieves the d-bus path.
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH

    def build_path(self, event: Event) -> str:
        """
        Retrieves the d-bus path for given event.
        :param event: The event.
        :type event: pythoneda.shared.Event
        :return: Such value.
        :rtype: str
        """
        return DBUS_PATH + "/" + event.name.replace("-", "_")

    @property
    def bus_type(self) -> str:
        """
        Retrieves the d-bus type.
        :return: Such value.
        :rtype: str
        """
        return BusType.SYSTEM

    @classmethod
    def transform(cls, event: CredentialProvided) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.runtime.secrets.events.CredentialProvided
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.name,
            event.value,
            json.dumps(event.metadata),
            event.id,
            json.dumps(event.previous_event_ids),
        ]

    @classmethod
    def sign(cls, event: CredentialProvided) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.runtime.secrets.events.CredentialProvided
        :return: The signature.
        :rtype: str
        """
        return "sssss"

    @classmethod
    def parse(cls, message: Message) -> CredentialProvided:
        """
        Parses given d-bus message containing a CredentialProvided event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The CredentialProvided event.
        :rtype: pythoneda.runtime.secrets.events.CredentialProvided
        """
        name, value, metadata, event_id, prev_event_ids = message.body
        return CredentialProvided(
            name,
            value,
            json.loads(metadata),
            event_id,
            json.loads(prev_event_ids),
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
