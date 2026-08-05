/**
  **************************************************************************************************
  * @ingroup   __MODULE_GROUP__
  * @file      __MODULE_PASCAL__.c
  * @version   Refer to __MODULE_PASCAL__.dox
  * @author    Genesys Electronics Design Team
  * @brief     This file contains the core implementation of the module.
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

/* PRIVATE COMPILE SWITCHES */

/* INCLUDE FILES */
#include "GDTypes.h"
#include "AppModules/AppModules.h"

#if (APP_MODULES_CONFIG__ENABLE___MODULE_INDEX_NAME__ == GD_TRUE)

#include "Error/Error.h"
#include "__MODULE_PASCAL__/__MODULE_PASCAL__.h"
#include "__MODULE_PASCAL__/__MODULE_PASCAL__Config.h"

/* PRIVATE LITERAL DEFINITIONS */

#define __MODULE_PASCAL____ReportError(Error_ptr, Cause)                                         \
   Error__Report(Error_ptr, ERROR__DOMAIN_PIOS_MIDDLEWARE,                                       \
      APP_MODULES____MODULE_INDEX_NAME___INDEX, Cause, __MODULE_SNAKE___CONFIG__ERROR_LEVEL)

/* PRIVATE TYPE DEFINITIONS */

/* PRIVATE CONSTANT DEFINITIONS */
// Note: #defines and ENUMs are located in "PRIVATE LITERAL DEFINITIONS".

/* PUBLIC CONSTANT DEFINITIONS */
// Note: public #defines and ENUMs are located in corresponding.h "PUBLIC LITERAL DEFINITIONS".

/* PRIVATE VARIABLE DEFINITIONS - defined as static */
// Note: These variables have global scope within this module but are not externalised.

/* PUBLIC VARIABLE DEFINITIONS */

/* PRIVATE FUNCTION DECLARATIONS */

/**
 * @brief      This function <function description>.
 *
 * @param      SomethingSpecific   Generically-typed variable which specifies something to be
 *                                 done.
 *
 * @return     GD_TRUE if implemented, GD_FALSE if not.
 */
static uint8_t DoSomethingPrivate1(uint8_t SomethingSpecific);

/**
 * @brief      This function <function description>.
 *
 * @return     genoError_t: standard error structure
 */
static genoError_t DoSomethingPrivate2(void);


/* PRIVATE FUNCTION DEFINITIONS */

/*
 * See above for doco
 */
static uint8_t DoSomethingPrivate1(uint8_t SomethingSpecific)
{
   (void) SomethingSpecific; // void if unused

   return GD_FALSE;
}

/*
 * See above for doco
 */
static genoError_t DoSomethingPrivate2(void)
{
   genoError_t error;
   Error__Init(&error);

   return error;
}

/* PUBLIC FUNCTION IMPLEMENTATIONS */

/*
 * See header for doco
 */
genoError_t __MODULE_PASCAL____DoSomethingPublic1(uint8_t SomethingSpecific)
{
   genoError_t error;
   Error__Init(&error);

   (void) SomethingSpecific; // void if unused

   error = DoSomethingPrivate2();

   return error;
}

/*
 * See header for doco
 */
genoError_t __MODULE_PASCAL____DoSomethingPublic2(uint8_t SomethingSpecific)
{
   genoError_t error;
   Error__Init(&error);

   if (DoSomethingPrivate1(SomethingSpecific) == GD_TRUE)
   {
      __MODULE_PASCAL____ReportError(&error, __MODULE_SNAKE____ERROR_CASE_1);
   }
   else
   {
      // Do nothing
   }

   return error;
}

#endif // (APP_MODULES_CONFIG__ENABLE___MODULE_INDEX_NAME__ == GD_TRUE)
