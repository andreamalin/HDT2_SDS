import pefile
pe = pefile.PE('sample_vg655_25th.exe')



print("[*] Listing APIs...")
for entry in pe.DIRECTORY_ENTRY_IMPORT:
	for API in entry.imports:
	    print('\t', API.name)
