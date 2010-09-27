# -*- coding: utf-8 -*-

"""
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License,
    or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, see <http://www.gnu.org/licenses/>.

    @author: mkaay
"""

from module.plugins.Account import Account

class MegauploadCom(Account):
    __name__ = "MegauploadCom"
    __version__ = "0.1"
    __type__ = "account"
    __description__ = """megaupload account plugin"""
    __author_name__ = ("RaNaN")
    __author_mail__ = ("RaNaN@pyload.org")

    def login(self, user, data):
        req = self.core.requestFactory.getRequest(self.__name__, user)
        req.load("http://www.megaupload.com/?c=login&next=c%3Dpremium", post={ "username" : user, "password" : data["password"], "login" :"1"}, cookies=True)