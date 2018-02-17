num_lines = 0

num_words = 0
num_chars = 0

listname = ('./processed/f9dffb73321870bf6150084d400cdb99.txt','./processed/f81f0a8863d96799127430d352b8570f.txt','./processed/fea2be6a9c57ddd7026b56029291b080.txt','./processed/f9dffb73321870bf6150084d400cdb99.txt','./processed/ea2dc97574e60ecb10171ec08afabeb7.txt','./processed/91f0ccb56b3daa6095ac19def910cefb.txt','./processed/c95f9367f4aaf444cb1d33c3f5f86ea5.txt','./processed/2e124b0f8e405b73483fa6364732a868.txt','./processed/75d0df4f758c79db48f58b50ebe100d5.txt','./processed/936767979808b7b3348a18366158559e.txt','./processed/7e36f66513f6cd8cae045e3e814bedd0.txt','./processed/af9ca261c6e9e3937080a10e9b86b92e.txt','./processed/edfb973265e499692a7e7c99b53bb0d3.txt','./processed/b80a31f3407973ba490c659e455f4b2f.txt','./processed/037160826799e0297a96f68263d6d2f8.txt','./processed/2d7dbd2c7c8445dc3110e31fc672f76e.txt','./processed/87dc88a24f7df480f2c2c9446544d997.txt','./processed/9247bd6f79d83171a7ee9d5369a2f4e5.txt','./processed/bb89434fca2452888675733c9962240b.txt','./processed/8205903d2dac0d551e1fff83188dbeb1.txt','./processed/001a9d2deb7d5d6a3c16f9af810507a3.txt','./processed/c14223918a5c2a3cdfb9c2154d34c671.txt','./processed/c8e808308c91b9ad13a66e313fa2f758.txt','./processed/c167cb1c7a2b9b71e9172e3066cc8f04.txt','./processed/00904fbc5bd5d5c14ef6500f0a74bf3f.txt','./processed/c239a4c290db73aff570122c75016cb1.txt','./processed/26af987d5e218fe0176a8fc7282a9a16.txt','./processed/049789604298104e20a89d342b1b2b9c.txt','./processed/2c0b21fad3c56dc25bbb2f22de445fe0.txt','./processed/df434559f215146a8f370d9c5f63fd05.txt')

for name in listname:
	num_lines = 0
	num_words = 0
	num_chars = 0
	with open(name, 'r') as f:
		fname = f.read().splitlines()
		for line in fname:
			words = line.split()
			num_lines += 1
			num_words += len(words)
			num_chars += len(line)
		print(name)
		print("Lines: ", num_lines,' Words: ',num_words,' Characters: ',num_chars)
