#!/bin/bash
# to run this script first -> chmod u+x build.sh

script="build.sh"
#Declare the number of mandatory args
margs=1

# Common functions - BEGIN
function example {
    echo -e "Example: $script -v 1.0\n"
}

function usage {
    echo -e "Usage: $script MANDATORY [V]\n"
}

function help {
  usage
    echo -e "MANDATORY:"
    echo -e "  -v, --version  VAL  Set the tag version for docker image\n"
  example
}

# Ensures that the number of passed args are at least equals
# to the declared number of mandatory args.
# It also handles the special case of the -h or --help arg.
function margs_precheck {
	if [ $2 ] && [ $1 -lt $margs ]; then
		if [ $2 == "--help" ] || [ $2 == "-h" ]; then
			help
			exit
		else
	    	usage
			example
	    	exit 1 # error
		fi
	fi
}

# Ensures that all the mandatory args are not empty
function margs_check {
	if [ $# -lt $margs ]; then
	    usage
	  	example
	    exit 1 # error
	fi
}
# Common functions - END

# Custom functions - BEGIN
# Put here your custom functions
# Custom functions - END

# Main
margs_precheck $# $1

marg0=

# Args while-loop
while [ "$1" != "" ];
do
   case $1 in
   -v  | --version )  shift
                          marg0=$1
                		  ;;
   -h   | --help )        help
                          exit
                          ;;
   *)                     
                          echo "$script: illegal option $1"
                          usage
						  example
						  exit 1 # error
                          ;;
    esac
    shift
done

# Pass here your mandatory args for check
margs_check $marg0

# rest of the script

read -p "Are you sure? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo '\n\n'
    echo '----------------------'
    echo '+ Building docker image'
    docker build --tag flaskback:$marg0 .
fi

exit 0