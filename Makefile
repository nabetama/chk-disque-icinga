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

install: rsync

rsync:
	rsync $(OPT) $(LOCAL_PATH)/ $(REMOTE_USER)@$(REMOTE_HOST):$(REMOTE_PATH)/
