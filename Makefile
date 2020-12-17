PRGM = wiggle
PREFIX ?= /usr
SHRDIR ?= $(PREFIX)/share
BINDIR ?= $(PREFIX)/bin

install:
	@install -Dm755 wiggle.py      $(DESTDIR)$(BINDIR)/$(PRGM)
