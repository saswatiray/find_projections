#!/bin/bash

if [ -z "$1" ]; then
    pycmd=$(which python 2> /dev/null)
elif [ -x "$1" ]; then
    pycmd="$1"
else
    echo "No python interpreter found, and none specified.  Aborting" 1>&2
    exit 1
fi

if [ -n "$pycmd" ]; then
    out=`"$pycmd" -c "import sys, os; \
                 s = os.path.join( sys.exec_prefix, 'lib', \
                                   'python%s' % str(sys.version[:3]), \
                                   'config', \
                                   'libpython%s.a' % str(sys.version[:3])); \
                 import distutils.sysconfig as sc; \
                 fn = sc.get_config_var; \
                 s += ' ' + fn('LIBS') + ' ' + fn('SYSLIBS'); \
                 s += ' ' + fn('LINKFORSHARED'); \
                 print s;"`
    if echo $out | grep -q "2.5"; then
        #force python 2.4 since ASL doesn't support 2.5 yet.
        #TODO(mjbaysek): rewrite so this block of code isn't duplicated
        pycmd="python2.4"
        out=`"$pycmd" -c "import sys, os; \
                     s = os.path.join( sys.exec_prefix, 'lib', \
                                     'python%s' % str(sys.version[:3]), \
                                     'config', \
                                     'libpython%s.a' % str(sys.version[:3])); \
                     import distutils.sysconfig as sc; \
                     fn = sc.get_config_var; \
                     s += ' ' + fn('LIBS') + ' ' + fn('SYSLIBS'); \
                     s += ' ' + fn('LINKFORSHARED'); \
                     print s;"`
    fi
    echo $out;

else
    echo "NO_PYTHON_AVAILABLE"
fi

