import logging as log

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('paciente.log'),
                    log.StreamHandler()
                ])

# Establecer el nivel de registro para el controlador de consola
log.getLogger().handlers[1].setLevel(log.INFO)  # Controlador de consola (StreamHandler)


if __name__ == "__main__":
    log.debug('Mensaje nivel debug')
    log.info('Mensaje nivel info')
    log.warning('Mensaje nivel warning')
    log.error('Mensjae nivel error')
    log.critical('Mensaje nivel critico')