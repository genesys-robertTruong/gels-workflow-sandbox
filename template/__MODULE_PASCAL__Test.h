/**
  **************************************************************************************************
  * @ingroup   __MODULE_GROUP__
  * @file      __MODULE_PASCAL__Test.h
  * @version   Refer to __MODULE_PASCAL__.dox
  * @author    Genesys Electronics Design Team
  * @brief     This file contains the public APIs and definitions for the module test routines.
  *            For details refer to @ref __MODULE_GROUP__ (__MODULE_PASCAL__.dox)
  *
  @verbatim
  **************************************************************************************************
   Copyright (c) __YEAR__, Genesys Electronics Design Pty Ltd
   All Rights Reserved
   Unit 5/33 Ryde Road
   Pymble NSW 2073
   Australia
   Telephone # +61-2-9496 8900

   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR
   IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
   FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
   DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
   DATA, OR PROFITS OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
   IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
   OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

  **************************************************************************************************
  @endverbatim
*/

/* COMPILER DIRECTIVES */
// Note: Warning/error ignorance must be commented.
#ifndef INCLUDED___MODULE_SNAKE___TEST_H_FILE
#define INCLUDED___MODULE_SNAKE___TEST_H_FILE


/* INCLUDE FILES */
#include "GDTypes.h"

/* PUBLIC COMPILE SWITCHES */

/* PUBLIC LITERAL DEFINITIONS */
#define __MODULE_SNAKE___TEST__RESERVED_INDEX                                  0U
#define __MODULE_SNAKE___TEST__UNIQUELY_NAMED_TEST_1                           1U
#define __MODULE_SNAKE___TEST__UNIQUELY_NAMED_TEST_2                           2U
#define __MODULE_SNAKE___TEST__NUMBER_OF_TESTS                                 2U

/* PUBLIC TYPE DEFINITIONS */

/* PUBLIC CONSTANT DECLARATIONS - declared as externs */

/* PUBLIC VARIABLE DECLARATIONS - declared as externs */

/* PUBLIC FUNCTION DECLARATIONS */

/**
 * @brief Runs the __MODULE_PASCAL__ monitor line
 *
 * @return     GD_TRUE if implemented, GD_FALSE if not.
 */
uint8_t __MODULE_PASCAL__Test__Monitor(void);

/**
 * @brief Runs through the __MODULE_PASCAL__ Command list
 *
 * @return     GD_TRUE if implemented, GD_FALSE if not.
 */
uint8_t __MODULE_PASCAL__Test__Command(void);

/**
 * @brief Runs test routines for the __MODULE_PASCAL__
 *
 * @param      Instance   The instance number.
 *
 * @param      TestNumber   The chosen test.
 *
 * @return     GD_TRUE if Test passed, GD_FALSE if not.
 */
uint8_t __MODULE_PASCAL__Test__Test(uint8_t Instance, uint8_t TestNumber);

#endif // INCLUDED___MODULE_SNAKE___TEST_H_FILE
