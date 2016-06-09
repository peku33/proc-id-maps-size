Introduction:
----------
Scans /proc/id/maps file and adds two columns
- Size in bytes
- Size in human readable form (B, KB, MB, GB)
Then passes it to output

Usage:
----------
`python ProcMapsSizeDump.py < /proc/id/maps`

Sample input / output:
----------

Input:
`55999a91c000-55999a9bd000 r-xp 00000000 ca:03 2198076                    /usr/bin/ssh`
`55999abbd000-55999abc0000 r--p 000a1000 ca:03 2198076                    /usr/bin/ssh`
`55999abc0000-55999abc1000 rw-p 000a4000 ca:03 2198076                    /usr/bin/ssh`
`55999abc1000-55999ac21000 rw-p 00000000 00:00 0                          [heap]`
`7fce07dc2000-7fce07dc7000 r-xp 00000000 ca:03 2178879                    /lib64/libnss_dns-2.22.so`
`7fce07dc7000-7fce07fc6000 ---p 00005000 ca:03 2178879                    /lib64/libnss_dns-2.22.so`
`7fce07fc6000-7fce07fc7000 r--p 00004000 ca:03 2178879                    /lib64/libnss_dns-2.22.so`
`7fce07fc7000-7fce07fc8000 rw-p 00005000 ca:03 2178879                    /lib64/libnss_dns-2.22.so`
`7fce07fc8000-7fce07fce000 r-xp 00000000 ca:03 2178883                    /lib64/libnss_db-2.22.so`
`7fce07fce000-7fce081cd000 ---p 00006000 ca:03 2178883                    /lib64/libnss_db-2.22.so`
`7fce081cd000-7fce081ce000 r--p 00005000 ca:03 2178883                    /lib64/libnss_db-2.22.so`
`7fce081ce000-7fce081cf000 rw-p 00006000 ca:03 2178883                    /lib64/libnss_db-2.22.so`
`7fce081cf000-7fce081d9000 r-xp 00000000 ca:03 2178882                    /lib64/libnss_files-2.22.so`
`7fce081d9000-7fce083d8000 ---p 0000a000 ca:03 2178882                    /lib64/libnss_files-2.22.so`
`7fce083d8000-7fce083d9000 r--p 00009000 ca:03 2178882                    /lib64/libnss_files-2.22.so`
`7fce083d9000-7fce083da000 rw-p 0000a000 ca:03 2178882                    /lib64/libnss_files-2.22.so`
`7fce083da000-7fce083e4000 r-xp 00000000 ca:03 2178905                    /lib64/libnss_nis-2.22.so`
`7fce083e4000-7fce085e3000 ---p 0000a000 ca:03 2178905                    /lib64/libnss_nis-2.22.so`
`7fce085e3000-7fce085e4000 r--p 00009000 ca:03 2178905                    /lib64/libnss_nis-2.22.so`
`7fce085e4000-7fce085e5000 rw-p 0000a000 ca:03 2178905                    /lib64/libnss_nis-2.22.so`
`7fce085e5000-7fce085f9000 r-xp 00000000 ca:03 2178902                    /lib64/libnsl-2.22.so`
`7fce085f9000-7fce087f9000 ---p 00014000 ca:03 2178902                    /lib64/libnsl-2.22.so`
`7fce087f9000-7fce087fa000 r--p 00014000 ca:03 2178902                    /lib64/libnsl-2.22.so`
`7fce087fa000-7fce087fb000 rw-p 00015000 ca:03 2178902                    /lib64/libnsl-2.22.so`
`7fce087fb000-7fce087fd000 rw-p 00000000 00:00 0`
`7fce087fd000-7fce08804000 r-xp 00000000 ca:03 2179000                    /lib64/libnss_compat-2.22.so`
`7fce08804000-7fce08a03000 ---p 00007000 ca:03 2179000                    /lib64/libnss_compat-2.22.so`
`7fce08a03000-7fce08a04000 r--p 00006000 ca:03 2179000                    /lib64/libnss_compat-2.22.so`
`7fce08a04000-7fce08a05000 rw-p 00007000 ca:03 2179000                    /lib64/libnss_compat-2.22.so`
`7fce08a05000-7fce08b97000 r-xp 00000000 ca:03 2178472                    /lib64/libc-2.22.so`
`7fce08b97000-7fce08d97000 ---p 00192000 ca:03 2178472                    /lib64/libc-2.22.so`
`7fce08d97000-7fce08d9b000 r--p 00192000 ca:03 2178472                    /lib64/libc-2.22.so`
`7fce08d9b000-7fce08d9d000 rw-p 00196000 ca:03 2178472                    /lib64/libc-2.22.so`
`7fce08d9d000-7fce08da1000 rw-p 00000000 00:00 0`
`7fce08da1000-7fce08db4000 r-xp 00000000 ca:03 2178878                    /lib64/libresolv-2.22.so`
`7fce08db4000-7fce08fb4000 ---p 00013000 ca:03 2178878                    /lib64/libresolv-2.22.so`
`7fce08fb4000-7fce08fb5000 r--p 00013000 ca:03 2178878                    /lib64/libresolv-2.22.so`
`7fce08fb5000-7fce08fb6000 rw-p 00014000 ca:03 2178878                    /lib64/libresolv-2.22.so`
`7fce08fb6000-7fce08fb8000 rw-p 00000000 00:00 0`
`7fce08fb8000-7fce08fcd000 r-xp 00000000 ca:03 3050135                    /lib64/libz.so.1.2.8`
`7fce08fcd000-7fce091cc000 ---p 00015000 ca:03 3050135                    /lib64/libz.so.1.2.8`
`7fce091cc000-7fce091cd000 r--p 00014000 ca:03 3050135                    /lib64/libz.so.1.2.8`
`7fce091cd000-7fce091ce000 rw-p 00015000 ca:03 3050135                    /lib64/libz.so.1.2.8`
`7fce091ce000-7fce091d0000 r-xp 00000000 ca:03 2178893                    /lib64/libdl-2.22.so`
`7fce091d0000-7fce093d0000 ---p 00002000 ca:03 2178893                    /lib64/libdl-2.22.so`
`7fce093d0000-7fce093d1000 r--p 00002000 ca:03 2178893                    /lib64/libdl-2.22.so`
`7fce093d1000-7fce093d2000 rw-p 00003000 ca:03 2178893                    /lib64/libdl-2.22.so`
`7fce093d2000-7fce09593000 r-xp 00000000 ca:03 2142749                    /usr/lib64/libcrypto.so.1.0.0`
`7fce09593000-7fce09793000 ---p 001c1000 ca:03 2142749                    /usr/lib64/libcrypto.so.1.0.0`
`7fce09793000-7fce097af000 r--p 001c1000 ca:03 2142749                    /usr/lib64/libcrypto.so.1.0.0`
`7fce097af000-7fce097ba000 rw-p 001dd000 ca:03 2142749                    /usr/lib64/libcrypto.so.1.0.0`
`7fce097ba000-7fce097be000 rw-p 00000000 00:00 0`
`7fce097be000-7fce097e0000 r-xp 00000000 ca:03 2179014                    /lib64/ld-2.22.so`
`7fce099d3000-7fce099d7000 rw-p 00000000 00:00 0`
`7fce099de000-7fce099df000 rw-p 00000000 00:00 0`
`7fce099df000-7fce099e0000 r--p 00021000 ca:03 2179014                    /lib64/ld-2.22.so`
`7fce099e0000-7fce099e1000 rw-p 00022000 ca:03 2179014                    /lib64/ld-2.22.so`
`7fce099e1000-7fce099e2000 rw-p 00000000 00:00 0`
`7ffe66680000-7ffe666a1000 rw-p 00000000 00:00 0                          [stack]`
`7ffe6676b000-7ffe6676d000 r--p 00000000 00:00 0                          [vvar]`
`7ffe6676d000-7ffe6676f000 r-xp 00000000 00:00 0                          [vdso]`
`ffffffffff600000-ffffffffff601000 r-xp 00000000 00:00 0                  [vsyscall]`

Output:
`55999a91c000-55999a9bd000           659456         644.00Kb r-xp 00000000 ca:03 2198076 /usr/bin/ssh`
`55999abbd000-55999abc0000            12288          12.00Kb r--p 000a1000 ca:03 2198076 /usr/bin/ssh`
`55999abc0000-55999abc1000             4096           4.00Kb rw-p 000a4000 ca:03 2198076 /usr/bin/ssh`
`55999abc1000-55999ac21000           393216         384.00Kb rw-p 00000000 00:00 0 [heap]`
`7fce07dc2000-7fce07dc7000            20480          20.00Kb r-xp 00000000 ca:03 2178879 /lib64/libnss_dns-2.22.so`
`7fce07dc7000-7fce07fc6000          2093056           2.00Mb ---p 00005000 ca:03 2178879 /lib64/libnss_dns-2.22.so`
`7fce07fc6000-7fce07fc7000             4096           4.00Kb r--p 00004000 ca:03 2178879 /lib64/libnss_dns-2.22.so`
`7fce07fc7000-7fce07fc8000             4096           4.00Kb rw-p 00005000 ca:03 2178879 /lib64/libnss_dns-2.22.so`
`7fce07fc8000-7fce07fce000            24576          24.00Kb r-xp 00000000 ca:03 2178883 /lib64/libnss_db-2.22.so`
`7fce07fce000-7fce081cd000          2093056           2.00Mb ---p 00006000 ca:03 2178883 /lib64/libnss_db-2.22.so`
`7fce081cd000-7fce081ce000             4096           4.00Kb r--p 00005000 ca:03 2178883 /lib64/libnss_db-2.22.so`
`7fce081ce000-7fce081cf000             4096           4.00Kb rw-p 00006000 ca:03 2178883 /lib64/libnss_db-2.22.so`
`7fce081cf000-7fce081d9000            40960          40.00Kb r-xp 00000000 ca:03 2178882 /lib64/libnss_files-2.22.so`
`7fce081d9000-7fce083d8000          2093056           2.00Mb ---p 0000a000 ca:03 2178882 /lib64/libnss_files-2.22.so`
`7fce083d8000-7fce083d9000             4096           4.00Kb r--p 00009000 ca:03 2178882 /lib64/libnss_files-2.22.so`
`7fce083d9000-7fce083da000             4096           4.00Kb rw-p 0000a000 ca:03 2178882 /lib64/libnss_files-2.22.so`
`7fce083da000-7fce083e4000            40960          40.00Kb r-xp 00000000 ca:03 2178905 /lib64/libnss_nis-2.22.so`
`7fce083e4000-7fce085e3000          2093056           2.00Mb ---p 0000a000 ca:03 2178905 /lib64/libnss_nis-2.22.so`
`7fce085e3000-7fce085e4000             4096           4.00Kb r--p 00009000 ca:03 2178905 /lib64/libnss_nis-2.22.so`
`7fce085e4000-7fce085e5000             4096           4.00Kb rw-p 0000a000 ca:03 2178905 /lib64/libnss_nis-2.22.so`
`7fce085e5000-7fce085f9000            81920          80.00Kb r-xp 00000000 ca:03 2178902 /lib64/libnsl-2.22.so`
`7fce085f9000-7fce087f9000          2097152           2.00Mb ---p 00014000 ca:03 2178902 /lib64/libnsl-2.22.so`
`7fce087f9000-7fce087fa000             4096           4.00Kb r--p 00014000 ca:03 2178902 /lib64/libnsl-2.22.so`
`7fce087fa000-7fce087fb000             4096           4.00Kb rw-p 00015000 ca:03 2178902 /lib64/libnsl-2.22.so`
`7fce087fb000-7fce087fd000             8192           8.00Kb rw-p 00000000 00:00 0`
`7fce087fd000-7fce08804000            28672          28.00Kb r-xp 00000000 ca:03 2179000 /lib64/libnss_compat-2.22.so`
`7fce08804000-7fce08a03000          2093056           2.00Mb ---p 00007000 ca:03 2179000 /lib64/libnss_compat-2.22.so`
`7fce08a03000-7fce08a04000             4096           4.00Kb r--p 00006000 ca:03 2179000 /lib64/libnss_compat-2.22.so`
`7fce08a04000-7fce08a05000             4096           4.00Kb rw-p 00007000 ca:03 2179000 /lib64/libnss_compat-2.22.so`
`7fce08a05000-7fce08b97000          1646592           1.57Mb r-xp 00000000 ca:03 2178472 /lib64/libc-2.22.so`
`7fce08b97000-7fce08d97000          2097152           2.00Mb ---p 00192000 ca:03 2178472 /lib64/libc-2.22.so`
`7fce08d97000-7fce08d9b000            16384          16.00Kb r--p 00192000 ca:03 2178472 /lib64/libc-2.22.so`
`7fce08d9b000-7fce08d9d000             8192           8.00Kb rw-p 00196000 ca:03 2178472 /lib64/libc-2.22.so`
`7fce08d9d000-7fce08da1000            16384          16.00Kb rw-p 00000000 00:00 0`
`7fce08da1000-7fce08db4000            77824          76.00Kb r-xp 00000000 ca:03 2178878 /lib64/libresolv-2.22.so`
`7fce08db4000-7fce08fb4000          2097152           2.00Mb ---p 00013000 ca:03 2178878 /lib64/libresolv-2.22.so`
`7fce08fb4000-7fce08fb5000             4096           4.00Kb r--p 00013000 ca:03 2178878 /lib64/libresolv-2.22.so`
`7fce08fb5000-7fce08fb6000             4096           4.00Kb rw-p 00014000 ca:03 2178878 /lib64/libresolv-2.22.so`
`7fce08fb6000-7fce08fb8000             8192           8.00Kb rw-p 00000000 00:00 0`
`7fce08fb8000-7fce08fcd000            86016          84.00Kb r-xp 00000000 ca:03 3050135 /lib64/libz.so.1.2.8`
`7fce08fcd000-7fce091cc000          2093056           2.00Mb ---p 00015000 ca:03 3050135 /lib64/libz.so.1.2.8`
`7fce091cc000-7fce091cd000             4096           4.00Kb r--p 00014000 ca:03 3050135 /lib64/libz.so.1.2.8`
`7fce091cd000-7fce091ce000             4096           4.00Kb rw-p 00015000 ca:03 3050135 /lib64/libz.so.1.2.8`
`7fce091ce000-7fce091d0000             8192           8.00Kb r-xp 00000000 ca:03 2178893 /lib64/libdl-2.22.so`
`7fce091d0000-7fce093d0000          2097152           2.00Mb ---p 00002000 ca:03 2178893 /lib64/libdl-2.22.so`
`7fce093d0000-7fce093d1000             4096           4.00Kb r--p 00002000 ca:03 2178893 /lib64/libdl-2.22.so`
`7fce093d1000-7fce093d2000             4096           4.00Kb rw-p 00003000 ca:03 2178893 /lib64/libdl-2.22.so`
`7fce093d2000-7fce09593000          1839104           1.75Mb r-xp 00000000 ca:03 2142749 /usr/lib64/libcrypto.so.1.0.0`
`7fce09593000-7fce09793000          2097152           2.00Mb ---p 001c1000 ca:03 2142749 /usr/lib64/libcrypto.so.1.0.0`
`7fce09793000-7fce097af000           114688         112.00Kb r--p 001c1000 ca:03 2142749 /usr/lib64/libcrypto.so.1.0.0`
`7fce097af000-7fce097ba000            45056          44.00Kb rw-p 001dd000 ca:03 2142749 /usr/lib64/libcrypto.so.1.0.0`
`7fce097ba000-7fce097be000            16384          16.00Kb rw-p 00000000 00:00 0`
`7fce097be000-7fce097e0000           139264         136.00Kb r-xp 00000000 ca:03 2179014 /lib64/ld-2.22.so`
`7fce099d3000-7fce099d7000            16384          16.00Kb rw-p 00000000 00:00 0`
`7fce099de000-7fce099df000             4096           4.00Kb rw-p 00000000 00:00 0`
`7fce099df000-7fce099e0000             4096           4.00Kb r--p 00021000 ca:03 2179014 /lib64/ld-2.22.so`
`7fce099e0000-7fce099e1000             4096           4.00Kb rw-p 00022000 ca:03 2179014 /lib64/ld-2.22.so`
`7fce099e1000-7fce099e2000             4096           4.00Kb rw-p 00000000 00:00 0`
`7ffe66680000-7ffe666a1000           135168         132.00Kb rw-p 00000000 00:00 0 [stack]`
`7ffe6676b000-7ffe6676d000             8192           8.00Kb r--p 00000000 00:00 0 [vvar]`
`7ffe6676d000-7ffe6676f000             8192           8.00Kb r-xp 00000000 00:00 0 [vdso]`
`ffffffffff600000-ffffffffff601000             4096           4.00Kb r-xp 00000000 00:00 0 [vsyscall]`
