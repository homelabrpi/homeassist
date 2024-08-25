entity_id = 'switch.smart_socket_socket'
entity_state = hass.states.get(entity_id)
logger.info(f"Current state of {entity_id} before toggle: {entity_state.state}")

# Call the input_boolean.toggle service
hass.services.call('switch', 'toggle', {'entity_id': entity_id})

# Log the state after toggling
entity_state_after = hass.states.get(entity_id)
logger.info(f"State of {entity_id} after toggle: {entity_state_after.state}")