#  Copyright 2008-2015 Nokia Solutions and Networks
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

try:
    import robotide.lib.robot as robot
except ImportError:
    pass
    
#import robotide.lib.robot.parsing.populators
#robotide.lib.robot.parsing.populators.PROCESS_CURDIR = False
import robot.parsing.populators
robot.parsing.populators.PROCESS_CURDIR = False



from robot.errors import DataError, Information
from robot.model import TagPatterns
from robot.output import LOGGER as ROBOT_LOGGER
from robot.output.loggerhelper import LEVELS as LOG_LEVELS
from robot.parsing.datarow import DataRow
from robot.parsing.model import (
    TestCase, TestDataDirectory, ResourceFile, TestCaseFile, UserKeyword,
    Variable, Step, ForLoop, VariableTable, KeywordTable, TestCaseTable,
    TestCaseFileSettingTable)
from robot.parsing.populators import FromFilePopulator
from robot.parsing.settings import (
    Library, Resource, Variables, Comment, _Import, Template,
    Fixture, Documentation, Timeout, Tags, Return)
from robot.parsing.tablepopulators import (
    UserKeywordPopulator, TestCasePopulator)
from robot.parsing.txtreader import TxtReader
from robot.running import TestLibrary, EXECUTION_CONTEXTS
from robot.libraries import STDLIBS as STDLIB_NAMES
from robot.running.usererrorhandler import UserErrorHandler
from robot.running.arguments.embedded import EmbeddedArgumentParser
from robot.utils import normpath, NormalizedDict
from robot.variables import Variables as RobotVariables
from robot.variables import is_scalar_var, is_list_var, is_var, is_dict_var,\
    VariableSplitter
from robot.variables.filesetter import VariableFileSetter
from robot.variables.tablesetter import VariableTableReader
from robot.version import get_version


ROBOT_VERSION = get_version()
