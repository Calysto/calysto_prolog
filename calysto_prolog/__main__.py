from IPython.kernel.zmq.kernelapp import IPKernelApp
from .kernel import PrologKernel
IPKernelApp.launch_instance(kernel_class=PrologKernel)
