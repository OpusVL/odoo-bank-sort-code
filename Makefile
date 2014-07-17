all:

clean_tempfiles:
	find bank_sort_code \( -name '*.py[co]' -or -name '*~' \) -print -delete
