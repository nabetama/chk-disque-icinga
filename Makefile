EXCLUDE=--exclude=.git
				--exclude=Makefile
				--exclude=Thumbs.db
				--exclude=.DS_Store
				--exclude=README.md 
				--exclude=Vagrantfile 
				--exclude=.vagrant/ 
				--exclude=requirements.txt

OPT=-cropgtv --cvs-exclude --delete $(EXCLUDE)
LOCAL_PATH=.
REMOTE_USER=vagrant
REMOTE_HOST=default
REMOTE_PATH=/home/vagrant/chk-disque/

default:
	@echo "Usage: "
	@echo "make install"
	@echo "make dry-install"

install: rsync
dry-install: dry-rsync

rsync:
	rsync $(OPT) $(LOCAL_PATH)/ $(REMOTE_USER)@$(REMOTE_HOST):$(REMOTE_PATH)/

dry-rsync:
»-$(MAKE) rsync OPT="--dry-run $(OPT)"
