#.PHONY : all clean rebuild
#
#all: ssd
#
#clean:
#	rm -f ssd *.o *~
#
#ssd: ssd.o flash.o  pagemap.o  hash.o   initialize.o
#	gcc-11  -g -o ssd $^ -lm
#%.o: %.c
#	gcc-11 -c  -g  $^ -o $@
#
#rebuild : clean all

.PHONY: all clean rebuild

# 使用 -m32 标志强制 32 位编译
CFLAGS = -m32 -g -D_FILE_OFFSET_BITS=64
LDFLAGS = -m32 -lm -D_FILE_OFFSET_BITS=64

all: ssd

clean:
	rm -f ssd *.o *~

ssd: ssd.o flash.o pagemap.o hash.o initialize.o insert_to_buffer.o
	gcc-11 $(LDFLAGS) -o $@ $^

%.o: %.c
	gcc-11 $(CFLAGS)  -c $^ -o $@

rebuild: clean all