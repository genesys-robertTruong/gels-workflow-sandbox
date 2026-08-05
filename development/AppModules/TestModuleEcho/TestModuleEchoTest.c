/**
  **************************************************************************************************
  * @ingroup   PM_99_95_TestModuleEcho
  * @file      TestModuleEchoTest.c
  * @version   Refer to TestModuleEcho.dox
  * @author    Genesys Electronics Design Team
  * @brief     This file contains the core implementation of the test functionality of the module.
  *            For details refer to @ref PM_99_95_TestModuleEcho (TestModuleEcho.dox)
  *
  @verbatim
  **************************************************************************************************
   Copyright (c) 2026, Genesys Electronics Design Pty Ltd
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
#include "TestModuleEcho/TestModuleEchoConfig.h"
#if ((TEST_MODULE_ECHO_CONFIG__COMPILE_TESTS == GD_TRUE) &&                                       \
     (APP_MODULES_CONFIG__ENABLE_PM_99_95_TEST_MODULE_ECHO == GD_TRUE))
#include "TestModuleEcho/TestModuleEcho.h"
#include "TestModuleEcho/TestModuleEchoTest.h"
#include "MessagesUtility/MessagesUtility.h"
#include "UnitTestManager/UnitTestManager.h"


/* PRIVATE LITERAL DEFINITIONS */


/* PRIVATE TYPE DEFINITIONS */


/* PRIVATE CONSTANT DEFINITIONS */


/* PUBLIC CONSTANT DEFINITIONS */


/* PRIVATE VARIABLE DEFINITIONS - defined as static */


/* PUBLIC VARIABLE DEFINITIONS */


/* PRIVATE FUNCTION DECLARATIONS */

static uint8_t UniquelyNamedTestX(uint8_t Instance);

/* PRIVATE FUNCTION DEFINITIONS */

static uint8_t UniquelyNamedTestX(uint8_t Instance)
{
   (void) Instance; // void if unused

   // Implement this!
   MessagesUtility__DebugNoTimeStamp(
      MESSAGES_UTILITY__IMPORTANT_MESSAGE, "Test 2 not implemented yet");

   return UNIT_TEST_MANAGER__TEST_NOT_TESTABLE;
}

/* PUBLIC FUNCTION IMPLEMENTATIONS */

uint8_t TestModuleEchoTest__Monitor(void)
{
   MessagesUtility__DebugNoTimeStamp(MESSAGES_UTILITY__IMPORTANT_MESSAGE,
         "TestModuleEcho Monitor not implemented");
   return GD_FALSE;
}


uint8_t TestModuleEchoTest__Command(void)
{
   MessagesUtility__DebugNoTimeStamp(MESSAGES_UTILITY__IMPORTANT_MESSAGE,
         "TestModuleEcho Command not implemented");
   return GD_FALSE;
}


uint8_t TestModuleEchoTest__Test(uint8_t Instance, uint8_t TestNumber)
{
   uint8_t testSuccess = UNIT_TEST_MANAGER__TEST_FAIL;

   (void) Instance; // void if unused

   MessagesUtility__DebugWithTimeStamp(MESSAGES_UTILITY__IMPORTANT_MESSAGE,
         "TestModuleEchoTest:\t*******************Running test %d**************************",
         TestNumber);

   switch (TestNumber)
   {
      case TEST_MODULE_ECHO_TEST__UNIQUELY_NAMED_TEST_1:
      {
         MessagesUtility__DebugNoTimeStamp(MESSAGES_UTILITY__IMPORTANT_MESSAGE,
               "Test 1 not implemented");
         testSuccess = UNIT_TEST_MANAGER__TEST_USER_CHECK;
         break;
      }
      case TEST_MODULE_ECHO_TEST__UNIQUELY_NAMED_TEST_2:
      {
         testSuccess = UniquelyNamedTestX(Instance);
         break;
      }
      default:
      {
         MessagesUtility__DebugNoTimeStamp(MESSAGES_UTILITY__IMPORTANT_MESSAGE,
               "Undefined Test Case: %u",TestNumber);
         break;
      }
   }

   return testSuccess;
}

#endif // (TEST_MODULE_ECHO_CONFIG__COMPILE_TESTS == GD_TRUE)
