# coding: utf-8
import os
from lib import TransitionEffect, Factory

parser = Factory.get_arg_parser()
parser.add_argument(
    '--state-file',
    default=os.environ['STATE_FILE'] if 'STATE_FILE' in os.environ else None
)
args = parser.parse_args()
logger = Factory.get_logger('SunsetStep', args)
fhem = Factory.get_fhem(args, logger)

if os.path.exists(args.state_file):
    with open(args.state_file, 'r') as fp:
        try:
            current_state = int(fp.read().strip())
        except ValueError:
            current_state = TransitionEffect.MAX_STATE
else:
    current_state = TransitionEffect.MAX_STATE

alpha = TransitionEffect.exponential(current_state)
logger.debug('Setting current_state=%i, alpha=%f' % (current_state, alpha))
fhem.rgb(alpha * 0xfd, alpha * 0x5e, alpha * 0x53)

if current_state == 0:
    os.remove(args.state_file)
else:
    with open(args.state_file, 'w') as fp:
        fp.write('%i' % (current_state - 1))
