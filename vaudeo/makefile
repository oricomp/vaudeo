ifneq ($(V),1)
	Q = @
endif


TOP=.
include ./makefile.vars


all : make_clean make_dirs

test : make_clean
	$(MAKE) -C $(TEST_DIR) TOPLEVEL=$(TOPLEVEL)


# Cleanup build artifacts
clean : make_clean

make_dirs :
	$(Q)mkdir -p $(SRC_DIR)
	$(Q)mkdir -p $(UTIL_DIR)
	$(Q)mkdir -p $(TEST_DIR)
	$(Q)mkdir -p $(BUILD_DIR)
	$(Q)mkdir -p $(BUILD_DIRS)

make_clean :
	$(Q)rm -f ./*.fs
	$(Q)rm -f ./*.o
	$(Q)rm -f ./*.json

.PHONY: clean program test make_clean
.INTERMEDIATE: toplevel.json toplevel_pnr.json $(TEST_OBJS)
