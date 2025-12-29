import React from 'react';
import { Github, Linkedin, Twitter, Globe, Mail, MapPin, Phone, ExternalLink, Download, Terminal, Award } from 'lucide-react';
import { Button } from '../../../components/ui/button';

const TechnicalTemplate = ({ data }) => {
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
    <div className="min-h-screen bg-gray-50 font-mono">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-6 py-4">
          <div className="flex justify-between items-center">
            <div className="flex items-center space-x-2">
              <Terminal className="w-6 h-6 text-gray-900" />
              <span className="text-xl font-bold text-gray-900">{user.name}</span>
            </div>
            <nav className="flex space-x-8">
              <a href="#about" className="text-gray-700 hover:text-gray-900">About</a>
              <a href="#skills" className="text-gray-700 hover:text-gray-900">Skills</a>
              <a href="#projects" className="text-gray-700 hover:text-gray-900">Projects</a>
              <a href="#contact" className="text-gray-700 hover:text-gray-900">Contact</a>
            </nav>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-6 py-12">
        {/* Hero Section */}
        <section id="about" className="mb-16">
          <div className="bg-white border border-gray-200 p-8 rounded-sm">
            <div className="flex items-start space-x-8">
              <img 
                src={user.profilePhoto} 
                alt={user.name}
                className="w-32 h-32 rounded-sm object-cover border border-gray-300"
              />
              <div className="flex-1">
                <h1 className="text-4xl font-bold text-gray-900 mb-2">{user.name}</h1>
                <p className="text-lg text-gray-700 mb-4">{user.bio}</p>
                <div className="flex flex-wrap gap-3 mb-4">
                  {user.location && (
                    <div className="flex items-center text-sm text-gray-600">
                      <MapPin className="w-4 h-4 mr-1" />
                      {user.location}
                    </div>
                  )}
                  {user.email && (
                    <div className="flex items-center text-sm text-gray-600">
                      <Mail className="w-4 h-4 mr-1" />
                      {user.email}
                    </div>
                  )}
                </div>
                <div className="flex items-center space-x-4">
                  {user.socialLinks?.github && (
                    <a href={user.socialLinks.github} target="_blank" rel="noopener noreferrer" className="text-gray-700 hover:text-gray-900">
                      <Github className="w-5 h-5" />
                    </a>
                  )}
                  {user.socialLinks?.linkedin && (
                    <a href={user.socialLinks.linkedin} target="_blank" rel="noopener noreferrer" className="text-gray-700 hover:text-gray-900">
                      <Linkedin className="w-5 h-5" />
                    </a>
                  )}
                  {user.socialLinks?.twitter && (
                    <a href={user.socialLinks.twitter} target="_blank" rel="noopener noreferrer" className="text-gray-700 hover:text-gray-900">
                      <Twitter className="w-5 h-5" />
                    </a>
                  )}
                  {user.socialLinks?.website && (
                    <a href={user.socialLinks.website} target="_blank" rel="noopener noreferrer" className="text-gray-700 hover:text-gray-900">
                      <Globe className="w-5 h-5" />
                    </a>
                  )}
                  {user.resumeUrl && (
                    <Button size="sm" variant="outline">
                      <Download className="w-4 h-4 mr-2" />
                      Resume
                    </Button>
                  )}
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Skills Section */}
        {skills.length > 0 && (
          <section id="skills" className="mb-16">
            <h2 className="text-3xl font-bold text-gray-900 mb-6">$ ./skills.sh</h2>
            <div className="bg-white border border-gray-200 p-8 rounded-sm">
              <div className="space-y-8">
                {Object.entries(groupedSkills).map(([category, categorySkills]) => (
                  <div key={category}>
                    <h3 className="text-xl font-bold text-gray-900 mb-4"># {category}</h3>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                      {categorySkills.map((skill) => (
                        <div key={skill.id} className="flex items-center justify-between">
                          <span className="text-gray-700">{skill.name}</span>
                          <div className="flex items-center space-x-2">
                            <div className="w-32 bg-gray-200 h-2 rounded-sm">
                              <div 
                                className="bg-gray-900 h-2 rounded-sm"
                                style={{ width: `${skill.level}%` }}
                              />
                            </div>
                            <span className="text-sm text-gray-600 w-12 text-right">{skill.level}%</span>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}

        {/* Projects Section */}
        {projects.length > 0 && (
          <section id="projects" className="mb-16">
            <h2 className="text-3xl font-bold text-gray-900 mb-6">$ ./projects.sh</h2>
            <div className="space-y-6">
              {projects.map((project) => (
                <div key={project.id} className="bg-white border border-gray-200 p-6 rounded-sm">
                  <div className="flex flex-col md:flex-row gap-6">
                    {project.image && (
                      <img 
                        src={project.image} 
                        alt={project.title}
                        className="w-full md:w-64 h-40 object-cover border border-gray-200 rounded-sm"
                      />
                    )}
                    <div className="flex-1">
                      <div className="flex items-start justify-between mb-2">
                        <h3 className="text-2xl font-bold text-gray-900">{project.title}</h3>
                        {project.featured && (
                          <span className="bg-gray-900 text-white text-xs px-2 py-1 rounded-sm">FEATURED</span>
                        )}
                      </div>
                      <p className="text-gray-700 mb-3">{project.description}</p>
                      {project.techStack && project.techStack.length > 0 && (
                        <div className="flex flex-wrap gap-2 mb-3">
                          {project.techStack.map((tech, index) => (
                            <span key={index} className="text-xs border border-gray-300 px-2 py-1 rounded-sm">
                              {tech}
                            </span>
                          ))}
                        </div>
                      )}
                      <div className="flex space-x-4">
                        {project.demoLink && (
                          <a href={project.demoLink} target="_blank" rel="noopener noreferrer" className="text-gray-700 hover:text-gray-900 flex items-center text-sm">
                            <ExternalLink className="w-4 h-4 mr-1" />
                            View Demo
                          </a>
                        )}
                        {project.githubLink && (
                          <a href={project.githubLink} target="_blank" rel="noopener noreferrer" className="text-gray-700 hover:text-gray-900 flex items-center text-sm">
                            <Github className="w-4 h-4 mr-1" />
                            Source Code
                          </a>
                        )}
                      </div>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Achievements Section */}
        {achievements.length > 0 && (
          <section id="achievements" className="mb-16">
            <h2 className="text-3xl font-bold text-gray-900 mb-6">$ ./achievements.sh</h2>
            <div className="bg-white border border-gray-200 p-8 rounded-sm">
              <div className="space-y-6">
                {achievements.map((achievement) => (
                  <div key={achievement.id} className="flex items-start space-x-4">
                    <div className="bg-gray-100 p-2 rounded-sm">
                      <Award className="w-5 h-5 text-gray-900" />
                    </div>
                    <div className="flex-1">
                      <h3 className="text-lg font-bold text-gray-900">{achievement.title}</h3>
                      <p className="text-sm text-gray-600">{achievement.issuer} | {achievement.date}</p>
                      {achievement.description && (
                        <p className="text-gray-700 mt-1">{achievement.description}</p>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}

        {/* Contact Section */}
        <section id="contact" className="mb-16">
          <h2 className="text-3xl font-bold text-gray-900 mb-6">$ ./contact.sh</h2>
          <div className="bg-white border border-gray-200 p-8 rounded-sm">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {user.email && (
                <div>
                  <div className="text-sm text-gray-600 mb-1">Email</div>
                  <div className="text-gray-900">{user.email}</div>
                </div>
              )}
              {user.phone && (
                <div>
                  <div className="text-sm text-gray-600 mb-1">Phone</div>
                  <div className="text-gray-900">{user.phone}</div>
                </div>
              )}
              {user.location && (
                <div>
                  <div className="text-sm text-gray-600 mb-1">Location</div>
                  <div className="text-gray-900">{user.location}</div>
                </div>
              )}
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-gray-200 py-6">
        <div className="max-w-7xl mx-auto px-6 text-center text-sm text-gray-600">
          <p>$ echo "&copy; 2025 {user.name}. Built with React."</p>
        </div>
      </footer>
    </div>
  );
};

export default TechnicalTemplate;