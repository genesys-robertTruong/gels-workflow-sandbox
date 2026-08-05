/**
 * Minimal seed AppModules.h for the GeLS workflow sandbox.
 * Structurally matches the real repo's registry format so
 * scaffold_module.py's register_header() regex finds and updates it.
 */

#ifndef INCLUDED_APPMODULES_H_FILE
#define INCLUDED_APPMODULES_H_FILE

#include "GDTypes.h"

#define APP_MODULES__RESERVED_MODULE                                       0U

#define APP_MODULES__PM_99_96_TEST_MODULE_DELTA_INDEX                      1U
#define APP_MODULES__PM_99_95_TEST_MODULE_ECHO_INDEX                       2U
#define APP_MODULES__PM_99_93_TEST_MODULE_GOLF_INDEX                       3U
#define APP_MODULES__NUMBER_OF_MODULES                                     4U

extern const char8_t* const AppModules__ModuleStringLookup_gro[APP_MODULES__NUMBER_OF_MODULES];

#endif /* INCLUDED_APPMODULES_H_FILE */
