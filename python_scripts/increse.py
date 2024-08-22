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

logger.info("increse was ok")