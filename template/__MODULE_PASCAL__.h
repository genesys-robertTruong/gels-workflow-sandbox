/**
  **************************************************************************************************
  * @ingroup   __MODULE_GROUP__
  * @file      __MODULE_PASCAL__.h
  * @version   Refer to __MODULE_PASCAL__.dox
  * @author    Genesys Electronics Design Team
  * @brief     This file contains the public APIs and definitions of the module.
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
#ifndef INCLUDED___MODULE_SNAKE___H_FILE
#define INCLUDED___MODULE_SNAKE___H_FILE

/* INCLUDE FILES */
#include "GDTypes.h"
#include "Error/Error.h"
#include "__MODULE_PASCAL__/__MODULE_PASCAL__Config.h"

/* PUBLIC COMPILE SWITCHES */

/* PUBLIC LITERAL DEFINITIONS */
#define __MODULE_SNAKE____NUMBER_OF_PUBLIC_PARTS         2U

#define __MODULE_SNAKE____INVALID_INSTANCE_ERROR         1U
#define __MODULE_SNAKE____INIT_ERROR                     2U
#define __MODULE_SNAKE____DEINIT_ERROR                   3U
#define __MODULE_SNAKE____NOT_INITIALISED_ERROR          4U
#define __MODULE_SNAKE____INTERFACE_ERROR                5U
#define __MODULE_SNAKE____INVALID_PARAMETER_ERROR        6U
#define __MODULE_SNAKE____ERROR_CASE_1                   7U
#define __MODULE_SNAKE____ERROR_CASE_2                   8U

/* PUBLIC TYPE DEFINITIONS */

/* PUBLIC CONSTANT DECLARATIONS - declared as externs */

/* PUBLIC VARIABLE DECLARATIONS - declared as externs */

/* PUBLIC FUNCTION DECLARATIONS */

/**
 * @brief      This function <function description>.
 *
 * @param      SomethingSpecific      generically-typed variable which specifies something to be
 *                                    done.
 *
 * @return     genoError_t: standard error structure
 */
genoError_t __MODULE_PASCAL____DoSomethingPublic1(uint8_t SomethingSpecific);

/**
 * @brief      This function <function description>.
 *
 * @param      SomethingSpecific      generically-typed variable which specifies something to be
 *                                    done.
 *
 * @return     genoError_t: standard error structure
 */
genoError_t __MODULE_PASCAL____DoSomethingPublic2(uint8_t SomethingSpecific);


#endif // INCLUDED___MODULE_SNAKE___H_FILE
