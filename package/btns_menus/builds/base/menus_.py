from btns_menus.builds.base.in_build import *

from typing import *
import discord
from discord import ui


class SingleDropMenu:
    def __init__(self, author: discord.Member, drop_menu1: SDropMenu, /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.menu1 = drop_menu1

        if self.menu1.author is None:
            self.menu1.update_one(self.author, "author")

        self.root_ = lambda: SingleDropMenu(self.author, self.menu1, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        if not self.menu1.hidden:
            view_.add_item(Menu(self.root_, self.menu1))

        return view_


class DuoDropMenu:
    def __init__(self, author: discord.Member, drop_menu1: SDropMenu, drop_menu2: SDropMenu,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.menus = [drop_menu1, drop_menu2]
        for menu_ in self.menus:
            if menu_.author is None:
                menu_.update_one(self.author, "author")

        self.root_ = lambda: DuoDropMenu(self.author, self.menus[0], self.menus[1], timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        for menu_ in self.menus:
            if not menu_.hidden:
                view_.add_item(Menu(self.root_, menu_))

        return view_


class TrioDropMenu:
    def __init__(self, author: discord.Member, drop_menu1: SDropMenu, drop_menu2: SDropMenu, drop_menu3: SDropMenu,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.menus = [drop_menu1, drop_menu2, drop_menu3]
        for menu_ in self.menus:
            if menu_.author is None:
                menu_.update_one(self.author, "author")

        self.root_ = lambda: TrioDropMenu(self.author, self.menus[0], self.menus[1], self.menus[2],
                                          timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        for menu_ in self.menus:
            if not menu_.hidden:
                view_.add_item(Menu(self.root_, menu_))

        return view_


class QuartetDropMenu:
    def __init__(self, author: discord.Member, drop_menu1: SDropMenu, drop_menu2: SDropMenu,
                 drop_menu3: SDropMenu, drop_menu4: SDropMenu,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.menus = [drop_menu1, drop_menu2, drop_menu3, drop_menu4]
        for menu_ in self.menus:
            if menu_.author is None:
                menu_.update_one(self.author, "author")

        self.root_ = lambda: QuartetDropMenu(self.author, self.menus[0], self.menus[1], self.menus[2], self.menus[3],
                                             timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        for menu_ in self.menus:
            if not menu_.hidden:
                view_.add_item(Menu(self.root_, menu_))

        return view_


class QuintetDropMenu:
    def __init__(self, author: discord.Member, drop_menu1: SDropMenu, drop_menu2: SDropMenu,
                 drop_menu3: SDropMenu, drop_menu4: SDropMenu, drop_menu5: SDropMenu,
                 /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout

        self.menus = [drop_menu1, drop_menu2, drop_menu3, drop_menu4, drop_menu5]
        for menu_ in self.menus:
            if menu_.author is None:
                menu_.update_one(self.author, "author")

        self.root_ = lambda: QuintetDropMenu(self.author, self.menus[0], self.menus[1], self.menus[2],
                                             self.menus[3], self.menus[4], timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        for menu_ in self.menus:
            if not menu_.hidden:
                view_.add_item(Menu(self.root_, menu_))

        return view_


class MultiDropMenu:
    def __init__(self, author: discord.Member, menus: List[SDropMenu], /, timeout: float = DEFAULT_TIMEOUT):
        self.author = author
        self.timeout = timeout
        self.menus = menus

        for menu_ in self.menus:
            if menu_.author is None:
                menu_.update(author=self.author)

        self.root_ = lambda: MultiDropMenu(self.author, self.menus, timeout=self.timeout)

    def view(self) -> ui.View:
        view_ = ui.View(timeout=self.timeout)
        for menu_ in self.menus:
            if not menu_.hidden:
                view_.add_item(Menu(self.root_, menu_))

        return view_