import React from 'react';
import { Github, Linkedin, Twitter, Globe, Mail, ExternalLink, Download } from 'lucide-react';

const MinimalTemplate = ({ data }) => {
  const { user, skills, projects, achievements } = data;

  // Group skills by category
  const groupedSkills = skills.reduce((acc, skill) => {
    if (!acc[skill.category]) {
      acc[skill.category] = [];
    }
    acc[skill.category].push(skill);
    return acc;
  }, {});

  return (
    <div className="min-h-screen bg-white">
      <div className="max-w-4xl mx-auto px-6 py-16">
        {/* Header */}
        <header className="mb-20">
          <div className="flex flex-col md:flex-row items-start gap-8 mb-8">
            <img 
              src={user.profilePhoto} 
              alt={user.name}
              className="w-32 h-32 rounded-full object-cover"
            />
            <div className="flex-1">
              <h1 className="text-5xl font-light text-gray-900 mb-4">{user.name}</h1>
              <p className="text-xl text-gray-600 leading-relaxed">{user.bio}</p>
            </div>
          </div>
          
          {/* Contact & Social */}
          <div className="flex flex-wrap items-center gap-6 text-gray-600">
            {user.email && (
              <a href={`mailto:${user.email}`} className="flex items-center hover:text-gray-900 transition-colors">
                <Mail className="w-4 h-4 mr-2" />
                {user.email}
              </a>
            )}
            {user.socialLinks?.github && (
              <a href={user.socialLinks.github} target="_blank" rel="noopener noreferrer" className="flex items-center hover:text-gray-900 transition-colors">
                <Github className="w-4 h-4 mr-2" />
                GitHub
              </a>
            )}
            {user.socialLinks?.linkedin && (
              <a href={user.socialLinks.linkedin} target="_blank" rel="noopener noreferrer" className="flex items-center hover:text-gray-900 transition-colors">
                <Linkedin className="w-4 h-4 mr-2" />
                LinkedIn
              </a>
            )}
            {user.socialLinks?.twitter && (
              <a href={user.socialLinks.twitter} target="_blank" rel="noopener noreferrer" className="flex items-center hover:text-gray-900 transition-colors">
                <Twitter className="w-4 h-4 mr-2" />
                Twitter
              </a>
            )}
            {user.socialLinks?.website && (
              <a href={user.socialLinks.website} target="_blank" rel="noopener noreferrer" className="flex items-center hover:text-gray-900 transition-colors">
                <Globe className="w-4 h-4 mr-2" />
                Website
              </a>
            )}
            {user.resumeUrl && (
              <button className="flex items-center hover:text-gray-900 transition-colors">
                <Download className="w-4 h-4 mr-2" />
                Resume
              </button>
            )}
          </div>
        </header>

        {/* Skills */}
        {skills.length > 0 && (
          <section className="mb-20">
            <h2 className="text-3xl font-light text-gray-900 mb-8 pb-4 border-b">Skills</h2>
            <div className="space-y-8">
              {Object.entries(groupedSkills).map(([category, categorySkills]) => (
                <div key={category}>
                  <h3 className="text-lg font-medium text-gray-700 mb-4">{category}</h3>
                  <div className="flex flex-wrap gap-3">
                    {categorySkills.map((skill) => (
                      <span 
                        key={skill.id}
                        className="px-4 py-2 text-sm text-gray-700 border border-gray-300 rounded-full"
                      >
                        {skill.name}
                      </span>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Projects */}
        {projects.length > 0 && (
          <section className="mb-20">
            <h2 className="text-3xl font-light text-gray-900 mb-8 pb-4 border-b">Projects</h2>
            <div className="space-y-16">
              {projects.map((project) => (
                <article key={project.id}>
                  {project.image && (
                    <img 
                      src={project.image} 
                      alt={project.title}
                      className="w-full h-80 object-cover mb-6 rounded-sm"
                    />
                  )}
                  <div className="flex items-start justify-between mb-3">
                    <h3 className="text-2xl font-light text-gray-900">{project.title}</h3>
                    {project.featured && (
                      <span className="text-xs text-gray-500 uppercase tracking-wide">Featured</span>
                    )}
                  </div>
                  <p className="text-gray-600 leading-relaxed mb-4">{project.description}</p>
                  {project.techStack && project.techStack.length > 0 && (
                    <div className="flex flex-wrap gap-2 mb-4">
                      {project.techStack.map((tech, index) => (
                        <span key={index} className="text-xs text-gray-500">
                          {tech}{index < project.techStack.length - 1 ? ' • ' : ''}
                        </span>
                      ))}
                    </div>
                  )}
                  <div className="flex space-x-6 text-sm">
                    {project.demoLink && (
                      <a 
                        href={project.demoLink} 
                        target="_blank" 
                        rel="noopener noreferrer"
                        className="flex items-center text-gray-700 hover:text-gray-900 transition-colors"
                      >
                        <ExternalLink className="w-4 h-4 mr-1" />
                        View Project
                      </a>
                    )}
                    {project.githubLink && (
                      <a 
                        href={project.githubLink} 
                        target="_blank" 
                        rel="noopener noreferrer"
                        className="flex items-center text-gray-700 hover:text-gray-900 transition-colors"
                      >
                        <Github className="w-4 h-4 mr-1" />
                        GitHub
                      </a>
                    )}
                  </div>
                </article>
              ))}
            </div>
          </section>
        )}

        {/* Achievements */}
        {achievements.length > 0 && (
          <section className="mb-20">
            <h2 className="text-3xl font-light text-gray-900 mb-8 pb-4 border-b">Achievements</h2>
            <div className="space-y-8">
              {achievements.map((achievement) => (
                <div key={achievement.id}>
                  <h3 className="text-xl font-light text-gray-900 mb-1">{achievement.title}</h3>
                  <p className="text-sm text-gray-600 mb-2">{achievement.issuer} • {achievement.date}</p>
                  {achievement.description && (
                    <p className="text-gray-600">{achievement.description}</p>
                  )}
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Footer */}
        <footer className="pt-12 border-t text-center">
          <p className="text-sm text-gray-500">&copy; 2025 {user.name}</p>
        </footer>
      </div>
    </div>
  );
};

export default MinimalTemplate;