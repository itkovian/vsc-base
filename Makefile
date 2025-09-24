NAME=vsc-base
VERSION=4.0.0
PREFIX=/opt/$(NAME)
VENV_DIR=$(PREFIX)/venv
BUILDROOT=$(PWD)/buildroot

BINARIES=

all: rpm

clean:
	rm -rf $(BUILDROOT) *.rpm

wheel:
	poetry build -f wheel

# Step 2: Create venv + install wheel into it
venv: wheel
		rm -rf $(BUILDROOT)
		mkdir -p $(BUILDROOT)$(PREFIX)
		python3 -m venv $(BUILDROOT)$(VENV_DIR)
		. $(BUILDROOT)$(VENV_DIR)/bin/activate && \
		    pip install --upgrade pip wheel && \
		    pip install dist/$(subst -,_,$(NAME))-$(VERSION)-*.whl

wrappers: venv
	mkdir -p $(BUILDROOT)/usr/bin
	for bin in $(BINARIES); do \
	    echo '#!/bin/bash' > $(BUILDROOT)/usr/bin/$$bin; \
	    echo 'exec $(VENV_DIR)/bin/$$bin "$$@"' >> $(BUILDROOT)/usr/bin/$$bin; \
	    chmod +x $(BUILDROOT)/usr/bin/$$bin; \
	done

rpm: wrappers
	fpm -s dir -t rpm \
	    -n $(NAME) \
	    -v $(VERSION) \
	    --prefix=/ \
	    -C $(BUILDROOT) .
