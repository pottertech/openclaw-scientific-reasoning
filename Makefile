PYTHON_BIN ?= python3

install:
	bash scripts/install.sh

verify:
	bash scripts/verify.sh

update:
	bash scripts/update.sh

update-lock:
	bash scripts/update.sh refresh-lock

register:
	bash scripts/register-capabilities.sh

unregister:
	bash scripts/unregister-capabilities.sh

uninstall:
	bash scripts/uninstall.sh --mode unregister_only

uninstall-full:
	bash scripts/uninstall.sh --mode full_remove

test:
	$(PYTHON_BIN) -m pytest -q

test-smoke:
	$(PYTHON_BIN) -m pytest -q tests/smoke

help:
	@echo "Targets:"
	@echo " install"
	@echo " verify"
	@echo " update"
	@echo " update-lock"
	@echo " register"
	@echo " unregister"
	@echo " uninstall"
	@echo " uninstall-full"
	@echo " test"
	@echo " test-smoke"
