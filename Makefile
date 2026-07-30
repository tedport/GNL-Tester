CC = gcc
PROJECT_PATH ?= ..
CFLAGS = -Wall -Werror -Wextra -g -fPIC -I$(PROJECT_PATH)/
LDFLAGS = -shared

# Allow variables to be overwritten by pytest
NAME ?= libgnl_test.so
BUFFER_SIZE ?= 4096
CFLAGS += -DBUFFER_SIZE=$(BUFFER_SIZE)

# Safely grab source files from the parent directory
ifndef BONUS
  SRC = $(PROJECT_PATH)/get_next_line.c $(PROJECT_PATH)/get_next_line_utils.c
else
  SRC = $(PROJECT_PATH)/get_next_line_bonus.c $(PROJECT_PATH)/get_next_line_utils_bonus.c
endif

ifndef AUTHORIZED_INVOKER
  $(error *** ERROR: This Makefile is must to be run by the automated testing tool. Direct execution is prohibited. ***)
endif

all: $(NAME)

 $(NAME): $(SRC)
	$(CC) $(LDFLAGS) $(CFLAGS) -o $@ $^

clean:
	rm -f libgnl*.so

fclean: clean

re: fclean all

.PHONY: all clean fclean re