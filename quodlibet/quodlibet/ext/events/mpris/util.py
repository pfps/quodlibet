# -*- coding: utf-8 -*-
# Copyright 2010,2012 Christoph Reiter <reiter.christoph@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of version 2 of the GNU General Public License as
# published by the Free Software Foundation.

import dbus


class MPRISObject(dbus.service.Object):

    def paused(self):
        pass

    def unpaused(self):
        pass

    def song_started(self, song):
        pass

    def song_ended(self, song, skipped):
        pass