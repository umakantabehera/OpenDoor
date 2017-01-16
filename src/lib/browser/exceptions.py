# -*- coding: utf-8 -*-

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Development Team: Stanislav Menshov
"""

class ThreadPoolError(Exception):
    """ThreadPoolError class"""

    def __init__(self, message):
        """
        Error message

        :param message: message
        :return: None
        """
        super(ThreadPoolError, self).__init__(message)

class WorkerError(Exception):
    """WorkerError class"""

    def __init__(self, message):
        """
        Error message

        :param message: message
        :return: None
        """
        super(WorkerError, self).__init__(message)

