import argparse
from Petgram import User

parser = argparse.ArgumentParser()
parser.add_argument('--n', type=int, default=5,
                    help='Number of users to create')
parser.add_argument('--type', type=str, default='user',
                    help='Type of data to create', choices=['user', 'post'])

args = parser.parse_args()

if __name__ == '__main__':
    user = User()

    try:
        for i in range(0, args.n):
            if args.type == 'user':
                user.createUser()
            elif args.type == 'post':
                print('Not implemented yet')
    except KeyboardInterrupt:
        print('Interrupted by user')
