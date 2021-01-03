#!/bin/bash -eu
# Copyright 2018 Google Inc.
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

# Build Liblouis
mkdir $SRC/liblouis/tests/fuzz
mv $SRC/table_fuzzer.cc $SRC/liblouis/tests/fuzz/
./autogen.sh
./configure
make -j$(nproc) V=1

cd tests/fuzz
cp ../tables/empty.ctb $OUT/
find ../.. -name "*.o" -exec ar rcs fuzz_lib.a {} \;
$CXX $CXXFLAGS -c table_fuzzer.cc -I/src/liblouis -o table_fuzzer.o
$CXX $CXXFLAGS $LIB_FUZZING_ENGINE table_fuzzer.o -o $OUT/table_fuzzer fuzz_lib.a

# Build corpus
zip $OUT/table_fuzzer_seed_corpus.zip $SRC/liblouis/tables/latinLetterDef6Dots.uti
