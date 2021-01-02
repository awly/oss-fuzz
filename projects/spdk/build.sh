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

# Build spdk
cd $SRC/spdk
export LDFLAGS="${CFLAGS}"
./scripts/pkgdep.sh
./configure --without-shared --without-isal
make -j$(nproc)

# Build fuzzers
cd $SRC/spdk/test/fuzz

$CXX $CXXFLAGS -I/src/spdk -I/src/spdk/include \
        -fPIC -c parse_json_fuzzer.cc -o parse_json_fuzzer.o

$CXX $CXXFLAGS $LIB_FUZZING_ENGINE \
	parse_json_fuzzer.o -o $OUT/parse_json_fuzzer \
        /src/spdk/build/lib/libspdk_env_dpdk.a \
        /src/spdk/build/lib/libspdk_json.a \
        ../../lib/json/json_parse.o

