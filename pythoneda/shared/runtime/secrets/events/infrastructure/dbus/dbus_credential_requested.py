# vim: set fileencoding=utf-8
"""
pythoneda/shared/runtime/secrets/events/infrastructure/dbus/dbus_credential_requested.py

This file defines the DbusCredentialRequested class.

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
from pythoneda.shared.runtime.secrets.events import CredentialRequested
from pythoneda.shared.runtime.secrets.events.infrastructure.dbus import DBUS_PATH
from typing import List


class DbusCredentialRequested(BaseObject, ServiceInterface):
    """
    D-Bus interface for CredentialRequested

    Class name: DbusCredentialRequested

    Responsibilities:
        - Define the d-bus interface for the CredentialRequested event.

    Collaborators:
        - None
    """

    def __init__(self):
        """
        Creates a new DbusCredentialRequested.
        """
        super().__init__("Pythoneda_Secrets_CredentialRequested")

    @signal()
    def CredentialRequested(self, name: "s", metadata: "s"):
        """
        Defines the CredentialRequested d-bus signal.
        :param name: The credential name.
        :type name: str
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
    def transform(cls, event: CredentialRequested) -> List[str]:
        """
        Transforms given event to signal parameters.
        :param event: The event to transform.
        :type event: pythoneda.runtime.secrets.events.CredentialRequested
        :return: The event information.
        :rtype: List[str]
        """
        return [
            event.name,
            json.dumps(event.metadata),
            json.dumps(event.previous_event_ids),
            event.id,
        ]

    @classmethod
    def sign(cls, event: CredentialRequested) -> str:
        """
        Retrieves the signature for the parameters of given event.
        :param event: The domain event.
        :type event: pythoneda.runtime.secrets.events.CredentialRequested
        :return: The signature.
        :rtype: str
        """
        return "ssss"

    @classmethod
    def parse(cls, message: Message) -> CredentialRequested:
        """
        Parses given d-bus message containing a CredentialRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :return: The CredentialRequested event.
        :rtype: pythoneda.runtime.secrets.events.CredentialRequested
        """
        name, metadata, prev_event_ids, event_id = message.body
        return CredentialRequested(
            name,
            json.loads(metadata),
            json.loads(prev_event_ids),
            event_id,
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
