import spike64  # pylint: disable=import-error

import targets
import testlib

class spike64_2(targets.Target):
    harts = [spike64.spike64_hart(misa=0x8000000000341129),
            spike64.spike64_hart(misa=0x8000000000341129)]
    openocd_config_path = "spike-2-hwthread.cfg"
    timeout_sec = 180
    implements_custom_test = True
    support_hasel = False
    support_memory_sampling = False # Needs SBA
    support_unavailable_control = True

    def create(self):
        return testlib.Spike(self, isa="RV64IMAFDV", abstract_rti=30,
                support_hasel=False, support_abstract_csr=False,
                vlen=512, elen=64)
