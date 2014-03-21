from __future__ import absolute_import
import threading, time, subprocess

from pytz import timezone

from django.conf import settings
from program.models import UserSettings, ContestSettings, ProblemResult

class TimeoutThread:
	def __init__(self, cmd):
		self.command 	= cmd
		self.process 	= None
		self.timeout 	= False

		self.stdin 		= None
		self.stdout 	= None
		self.stderr 	= None
		self.exitCode 	= None
	def run(self, stdin, timeout):
		def target():
			self.process = subprocess.Popen(self.command, 
				stdin = subprocess.PIPE, stdout = subprocess.PIPE,
				stderr = subprocess.PIPE)
			(self.stdout, self.stderr) = self.process.communicate(input=stdin)
			self.exitCode = self.process.returncode

		thread = threading.Thread(target=target)
		thread.start()

		thread.join(timeout)
		if thread.is_alive():
			self.process.terminate()
			thread.join()
			self.timeout = True

class SolutionValidator:
	def __init__(self, problem, solution):
		self.problem = problem
		self.solution = solution
		# self.problemResult = None
		# self.executionResult = None

		self.executed 	= False
		self.successful = False
		self.command 	= []

		self.initCommand();
		self.initEnv();

		self.thread = TimeoutThread(self.command)

		self.setStdin();
		self.setStdout();
		self.setStderr();

	def initCommand(self):
		self.command = ["python", self.solution.solution.path]

	# def setStdin, setStdout, setStderr
	def setStdin(self):
		pass
		self.stdin = self.problem.inputSubmit
	def setStdout(self):
		pass
	def setStderr(self):
		pass

	def initEnv(self):
		self.TIMEOUT = 5

	def execute(self):
		self.thread.run(self.stdin, self.TIMEOUT)



	def successful(self):
		return self.executed and self.thread.timeout

	def timeout():
		return self.timeout

	@staticmethod
	def validate(problem, executionResult):
		exitCodeCorrect = executionResult.exitCode == 0
		stdoutMatch = SolutionValidator._compareStdout(executionResult.stdout, problem.outputSubmit)

		return exitCodeCorrect and stdoutMatch

	@staticmethod
	def _compareStdout(actual, expected):
		cleanActual = unicode(actual.replace("\r", u""))
		cleanExpected = unicode(expected.replace("\r", u""))
		returnVal = cleanActual == cleanExpected
		return returnVal



# Site-wide Context Processor
def programSiteContext(request):
	siteContext = {}

	# Wire in UserSettings Object
	if request.user.is_authenticated():
		try:
			siteContext['userdata'] = UserSettings.objects.get(user=request.user)
		except UserSettings.DoesNotExist:
			pass

	# Wire in ContestSettings Object
	siteContext['contest'] = ContestSettings.objects.get(pk=1)

	#wire contest end time
	siteContext['contestEndTimestamp'] = siteContext['contest'].endTime.astimezone(timezone(settings.TIME_ZONE)).isoformat()

	return siteContext




