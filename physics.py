def resolve_collision(a1, a2):
        # Vector between centers
        delta = a2.position - a1.position
        distance = delta.length()
        if distance == 0:
            return

        # Normalize collision normal
        normal = delta / distance

        # Relative velocity
        rel_vel = a1.velocity - a2.velocity
        vel_along_normal = rel_vel.dot(normal)

        if vel_along_normal > 0:
            return  # They're moving apart

        # Masses
        m1 = a1.radius ** 2
        m2 = a2.radius ** 2

        # Elastic impulse
        impulse = (2 * vel_along_normal) / (m1 + m2)
        a1.velocity -= impulse * m2 * normal
        a2.velocity += impulse * m1 * normal

def push_apart(a1, a2):
    delta = a2.position - a1.position
    distance = max(delta.length(), 0.001)
    overlap = (a1.radius + a2.radius) - distance
    correction = delta.normalize() * (overlap / 2)
    a1.position -= correction
    a2.position += correction

