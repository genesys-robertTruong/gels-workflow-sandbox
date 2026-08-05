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
   "PM_99_50_TEST_MODULE_KILO",                      // 1
   "PM_99_51_TEST_MODULE_LIMA",                      // 2
#else
   "0",
   "1",
   "2",
#endif // APPMODULES_CONFIG__COMPILE_MODULE_NAMES
};
#endif // APP_MODULES_CONFIG__ENABLE_AM_01_01_APPMODULES
