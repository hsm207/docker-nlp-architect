import argparse
from pathlib import Path
from collections import namedtuple
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

BackendConfig = namedtuple('BackendConfig', ['base_image', 'requirements_mod'])

gpu_config = BackendConfig(base_image='tensorflow/tensorflow:1.12.0-gpu-py3',
                           requirements_mod="sed -i 's/tensorflow==/tensorflow-gpu==/' requirements.txt")
cpu_config = BackendConfig(base_image='tensorflow/tensorflow:1.12.0-py3',
                           requirements_mod=':')

backend_options = {
    'cpu': cpu_config,
    'gpu': gpu_config
}


def main(args):
    backend_choice = backend_options[args.backend]

    dockerfiles_dir = Path('./dockerfiles')

    with open(dockerfiles_dir / 'Dockerfile.template') as f:
        dockerfile_template = f.read()

    dockerfile_template = dockerfile_template.replace('%%BASEIMAGE%%', backend_choice.base_image)
    dockerfile_template = dockerfile_template.replace('%%REQMOD%%', backend_choice.requirements_mod)

    output_file = dockerfiles_dir / f'nlp-architect-{args.backend}.Dockerfile'

    with open(output_file, 'w') as f:
        f.write(dockerfile_template)

    logging.info(f'Created dockerfile for nlp architect with {args.backend} backend at {output_file.resolve()}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Build a dockerfile containing Intel\'s NLP Architect with CPU '
                                                 'or GPU backend.')

    parser.add_argument('--backend',
                        type=str,
                        required=True,
                        choices=['cpu', 'gpu'],
                        help='The backend to use when installing NLP Architect. Can be either cpu or gpu.')

    args = parser.parse_args()
    main(args)
