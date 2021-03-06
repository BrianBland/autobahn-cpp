###############################################################################
#
# Copyright (c) Tavendo GmbH
#
# Boost Software License - Version 1.0 - August 17th, 2003
#
# Permission is hereby granted, free of charge, to any person or organization
# obtaining a copy of the software and accompanying documentation covered by
# this license (the "Software") to use, reproduce, display, distribute,
# execute, and transmit the Software, and to prepare derivative works of the
# Software, and to permit third-parties to whom the Software is furnished to
# do so, all subject to the following:
#
# The copyright notices in the Software and this entire statement, including
# the above license grant, this restriction and the following disclaimer,
# must be included in all copies of the Software, in whole or in part, and
# all derivative works of the Software, unless such copies or derivative
# works are solely in the form of machine-executable object code generated by
# a source language processor.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
# SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
# FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
#
###############################################################################

if __name__ == "__main__":

   import sys
   import argparse
   import mimetypes

   from twisted.python import log
   from twisted.internet import reactor
   from twisted.web.server import Site
   from twisted.web.static import File
   from twisted.internet.endpoints import serverFromString

   mimetypes.add_type('image/svg+xml', '.svg')
   mimetypes.add_type('text/javascript', '.jgz')

   parser = argparse.ArgumentParser()

   parser.add_argument("--root", type = str, default = ".",
                       help = 'Web document root directory')

   parser.add_argument("--endpoint", type = str, default = "tcp:8080",
                       help = 'Twisted server endpoint descriptor, e.g. "tcp:8080" or "unix:/tmp/mywebsocket".')

   parser.add_argument("-s", "--silence", action = "store_true",
                       help = "Disable access logging.")

   args = parser.parse_args()
   log.startLogging(sys.stdout)

   factory = Site(File(args.root))
   if args.silence:
      factory.log = lambda _: None
      factory.noisy = False

   server = serverFromString(reactor, args.endpoint)
   server.listen(factory)

   reactor.run()
