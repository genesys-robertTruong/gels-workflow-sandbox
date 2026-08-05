/**
 * Minimal seed AppModules.h for the GeLS workflow sandbox.
 * Structurally matches the real repo's registry format so
 * scaffold_module.py's register_header() regex finds and updates it.
 */

#ifndef INCLUDED_APPMODULES_H_FILE
#define INCLUDED_APPMODULES_H_FILE

#include "GDTypes.h"

#define APP_MODULES__RESERVED_MODULE                                       0U

#define APP_MODULES__PM_99_99_TEST_MODULE_ALPHA_INDEX                      1U
#define APP_MODULES__NUMBER_OF_MODULES                                     2U

extern const char8_t* const AppModules__ModuleStringLookup_gro[APP_MODULES__NUMBER_OF_MODULES];

#endif /* INCLUDED_APPMODULES_H_FILE */
