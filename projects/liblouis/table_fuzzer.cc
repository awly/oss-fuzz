/*
# Copyright 2021 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################
*/

#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>
#include "../../liblouis/liblouis.h"
#include <filesystem>

extern "C" int
LLVMFuzzerTestOneInput(const uint8_t *data, size_t size)
{
	char new_file[256];
	sprintf(new_file, "/tmp/libfuzzer.uti");

	FILE *fp = fopen(new_file, "wb");
	if (!fp)
		return 0;
	fwrite(data, size, 1, fp);
	fclose(fp);

	char *table = "empty.ctb";
	lou_compileString(table, "include /tmp/libfuzzer.uti");

	lou_free();
	std::__fs::filesystem::remove_all("/tmp/libfuzzer.uti");

	return 0;
}
