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
from dbus_next import Message
from dbus_next.service import signal
import json
from pythoneda.shared import Event, Invariants, PythonedaApplication
from pythoneda.shared.infrastructure.dbus import DbusEvent
from pythoneda.shared.runtime.secrets.events import CredentialRequested
from pythoneda.shared.runtime.secrets.events.infrastructure.dbus import DBUS_PATH
from typing import List, Tuple, Type


class DbusCredentialRequested(DbusEvent):
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
        super().__init__(DBUS_PATH)

    @classmethod
    @property
    def name(cls) -> str:
        """
        Retrieves the d-bus interface name.
        :return: Such value.
        :rtype: str
        """
        return "Pythoneda_Secrets_CredentialRequested"

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

    def build_path(self, event: Event) -> str:
        """
        Retrieves the d-bus path for given event.
        :param event: The event.
        :type event: pythoneda.shared.Event
        :return: Such value.
        :rtype: str
        """
        return self.path

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
            Invariants.instance().to_json(event),
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
        return "sssss"

    @classmethod
    def parse(
        cls, message: Message, app: PythonedaApplication
    ) -> Tuple[str, CredentialRequested]:
        """
        Parses given d-bus message containing a CredentialRequested event.
        :param message: The message.
        :type message: dbus_next.Message
        :param app: The application instance.
        :type app: pythoneda.shared.PythonedaApplication
        :return: A tuple with the serialized invariants and the CredentialRequested event.
        :rtype: Tuple[str, pythoneda.runtime.secrets.events.CredentialRequested]
        """
        name, metadata, prev_event_ids, invariants, event_id = message.body
        return (
            invariants,
            CredentialRequested(
                name,
                json.loads(metadata),
                json.loads(prev_event_ids),
                event_id,
            ),
        )

    @classmethod
    def event_class(cls) -> Type[Event]:
        """
        Retrieves the specific event class.
        :return: Such class.
        :rtype: type(pythoneda.shared.Event)
        """
        return CredentialRequested


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
