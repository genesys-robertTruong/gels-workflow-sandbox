/**
 * Minimal seed AppModules.c for the GeLS workflow sandbox.
 * Structurally matches the real repo's registry format so
 * scaffold_module.py's register_source() regex finds and updates it.
 */

#include "AppModules/AppModules.h"

#if (APP_MODULES_CONFIG__ENABLE_AM_01_01_APPMODULES == GD_TRUE)
const char8_t *const AppModules__ModuleStringLookup_gro[APP_MODULES__NUMBER_OF_MODULES] = {
#if (APP_MODULES_CONFIG__COMPILE_MODULE_NAMES == GD_TRUE)
   "APP_MODULES__RESERVED_MODULE",                   // 0
   "PM_99_96_TEST_MODULE_DELTA",                     // 1
   "PM_99_95_TEST_MODULE_ECHO",                      // 2
   "PM_99_92_TEST_MODULE_HOTEL",                     // 3
   "PM_99_91_TEST_MODULE_INDIA",                     // 4
   "PM_99_90_TEST_MODULE_JULIET",                    // 5
#else
   "0",
   "1",
   "2",
   "3",
   "4",
   "5",
#endif // APPMODULES_CONFIG__COMPILE_MODULE_NAMES
};
#endif // APP_MODULES_CONFIG__ENABLE_AM_01_01_APPMODULES
