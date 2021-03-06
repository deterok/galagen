#-*-coding:utf-8-*-
#===============================================================================
# 	Copyright 2012 Vadim Suharnikov <v.suharnikov@gmail.com>
#
#	This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================


from pylab import *
from galagen import galaxy_generator

if __name__ == '__main__':
	x, y = galaxy_generator().speral_galaxy(arms=4)
	plot(x, y, 'bo')
	show()