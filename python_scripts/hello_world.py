# `data` is available as builtin and is a dictionary with the input data.
name = data.get("name", "world")
# `logger` and `time` are available as builtin without the need of explicit import.
logger.info("Hello {} at {}".format(name, time.time()))

entity_id = 'sensor.custom_entity'
entity_state = hass.states.get(entity_id)
current_value = 0
if entity_state:
    current_value = entity_state.state
    # Optionally convert the state to an integer if it's a number
    try:
        current_value = int(current_value)
    except ValueError:
        # Handle the case where the state cannot be converted to an integer
        current_value = 0
state_value = current_value + 1

# Set the state of the entity
hass.states.set(entity_id, state_value, {
    'friendly_name': 'Custom Entity',
    'unit_of_measurement': 'units',
    'icon': 'mdi:thermometer'
})

switch_entity_id = 'switch.smart_socket_socket'

switch_state = hass.states.get(switch_entity_id)

if switch_state:
    # If the switch is currently on, turn it off; otherwise, turn it on
    if switch_state.state == 'on':
        logger.info("Switch is currently ON. Turning it OFF.")
        hass.services.call('switch', 'turn_off', {'entity_id': switch_entity_id})
    else:
        logger.info("Switch is currently OFF. Turning it ON.")
        hass.services.call('switch', 'turn_on', {'entity_id': switch_entity_id})
else:
    logger.warning("Entity {} not found".format(switch_entity_id))


output["hello"] = f"hello {data.get('name', 'world')}"