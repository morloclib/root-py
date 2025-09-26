test:
	morloc make test.loc
	./nexus test

clean:
	rm -rf __pycache__ nexus nexus.c pool*
