from django.core.management.base import BaseCommand
from main.models import TeamMember, Project

class Command(BaseCommand):
    help = 'Create sample team members and projects'

    def handle(self, *args, **options):
        # Create sample team members
        team_members_data = [
            {
                'name': 'Sarah Johnson',
                'position': 'Senior Full-Stack Developer',
                'bio': 'Passionate full-stack developer with 8+ years of experience in building scalable web applications. Specializes in React, Python, and cloud architecture.',
                'email': 'sarah@techcorp.com',
                'linkedin': 'https://linkedin.com/in/sarahjohnson',
                'github': 'https://github.com/sarahjohnson',
                'skills': 'React, Python, Django, AWS, PostgreSQL, Docker, TypeScript',
                'experience_years': 8,
            },
            {
                'name': 'Michael Chen',
                'position': 'Mobile App Developer',
                'bio': 'Expert mobile developer creating beautiful, performant apps for iOS and Android. Focused on user experience and cutting-edge mobile technologies.',
                'email': 'michael@techcorp.com',
                'linkedin': 'https://linkedin.com/in/michaelchen',
                'github': 'https://github.com/michaelchen',
                'skills': 'React Native, Flutter, Swift, Kotlin, Firebase, Redux',
                'experience_years': 6,
            },
            {
                'name': 'Emily Rodriguez',
                'position': 'UI/UX Designer & Frontend Developer',
                'bio': 'Creative designer and frontend developer who bridges the gap between design and development. Creates intuitive user experiences that drive engagement.',
                'email': 'emily@techcorp.com',
                'linkedin': 'https://linkedin.com/in/emilyrodriguez',
                'github': 'https://github.com/emilyrodriguez',
                'skills': 'Figma, React, Vue.js, Tailwind CSS, SCSS, Adobe Creative Suite',
                'experience_years': 5,
            },
            {
                'name': 'David Kim',
                'position': 'DevOps Engineer',
                'bio': 'Infrastructure specialist ensuring reliable, scalable deployments. Expert in cloud platforms, containerization, and CI/CD pipelines.',
                'email': 'david@techcorp.com',
                'linkedin': 'https://linkedin.com/in/davidkim',
                'github': 'https://github.com/davidkim',
                'skills': 'AWS, Docker, Kubernetes, Terraform, Jenkins, MongoDB',
                'experience_years': 7,
            },
        ]

        for member_data in team_members_data:
            member, created = TeamMember.objects.get_or_create(
                email=member_data['email'],
                defaults=member_data
            )
            if created:
                self.stdout.write(f'Created team member: {member.name}')
                
                # Create sample projects for each team member
                if member.name == 'Sarah Johnson':
                    projects = [
                        {
                            'title': 'E-commerce Platform',
                            'description': 'Full-featured e-commerce platform with payment integration, inventory management, and analytics dashboard.',
                            'technologies': 'Django, React, PostgreSQL, Stripe, AWS',
                            'project_url': 'https://example-ecommerce.com',
                            'github_url': 'https://github.com/sarahjohnson/ecommerce-platform',
                        },
                        {
                            'title': 'Task Management System',
                            'description': 'Collaborative task management application with real-time updates and team collaboration features.',
                            'technologies': 'React, Node.js, Socket.io, MongoDB',
                            'project_url': 'https://example-tasks.com',
                            'github_url': 'https://github.com/sarahjohnson/task-manager',
                        }
                    ]
                elif member.name == 'Michael Chen':
                    projects = [
                        {
                            'title': 'Fitness Tracking App',
                            'description': 'Cross-platform mobile app for fitness tracking with social features and workout plans.',
                            'technologies': 'React Native, Firebase, Redux, Expo',
                            'project_url': 'https://example-fitness.com',
                            'github_url': 'https://github.com/michaelchen/fitness-app',
                        }
                    ]
                elif member.name == 'Emily Rodriguez':
                    projects = [
                        {
                            'title': 'Design System Library',
                            'description': 'Comprehensive design system and component library for consistent user interfaces.',
                            'technologies': 'React, Storybook, Tailwind CSS, Figma',
                            'project_url': 'https://example-design-system.com',
                            'github_url': 'https://github.com/emilyrodriguez/design-system',
                        }
                    ]
                else:  # David Kim
                    projects = [
                        {
                            'title': 'Cloud Infrastructure',
                            'description': 'Scalable cloud infrastructure setup with automated deployment and monitoring.',
                            'technologies': 'AWS, Terraform, Docker, Kubernetes, Jenkins',
                            'github_url': 'https://github.com/davidkim/cloud-infrastructure',
                        }
                    ]
                
                for project_data in projects:
                    project_data['team_member'] = member
                    Project.objects.create(**project_data)
                    self.stdout.write(f'Created project: {project_data["title"]}')

        self.stdout.write(self.style.SUCCESS('Successfully created sample data'))