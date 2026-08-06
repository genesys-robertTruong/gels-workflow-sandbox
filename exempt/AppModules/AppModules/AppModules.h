/**
 * Minimal seed AppModules.h for the GeLS workflow sandbox.
 * Structurally matches the real repo's registry format so
 * scaffold_module.py's register_header() regex finds and updates it.
 */

#ifndef INCLUDED_APPMODULES_H_FILE
#define INCLUDED_APPMODULES_H_FILE

#include "GDTypes.h"

#define APP_MODULES__RESERVED_MODULE                                       0U

#define APP_MODULES__PM_99_50_TEST_MODULE_KILO_INDEX                       1U
#define APP_MODULES__PM_99_51_TEST_MODULE_LIMA_INDEX                       2U
#define APP_MODULES__PM_99_52_TEST_MODULE_MIKE_INDEX                       3U
#define APP_MODULES__PM_99_53_TEST_MODULE_NOVEMBER_INDEX                   4U
#define APP_MODULES__PM_99_54_TEST_MODULE_OSCAR_INDEX                      5U
#define APP_MODULES__NUMBER_OF_MODULES                                     6U

extern const char8_t* const AppModules__ModuleStringLookup_gro[APP_MODULES__NUMBER_OF_MODULES];

#endif /* INCLUDED_APPMODULES_H_FILE */
