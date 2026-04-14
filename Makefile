.PHONY: install verify update update-lock uninstall uninstall-full test clean

install:
	bash scripts/install.sh

verify:
	bash scripts/verify.sh

update:
	bash scripts/update.sh

update-lock:
	bash scripts/update.sh refresh-lock

uninstall:
	bash scripts/uninstall.sh --mode unregister_only

uninstall-full:
	bash scripts/uninstall.sh --mode full_remove

test:
	pytest -q

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true