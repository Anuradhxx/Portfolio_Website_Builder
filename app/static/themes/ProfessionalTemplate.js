import React from 'react';
import { Github, Linkedin, Twitter, Globe, Mail, MapPin, Phone, ExternalLink, Download, Award, Briefcase } from 'lucide-react';
import { Button } from '../../../components/ui/button';

const ProfessionalTemplate = ({ data }) => {
  const { user, skills, projects, achievements } = data;

  return (
    <div className="min-h-screen bg-white">
      {/* Header */}
      <header className="bg-gray-900 text-white py-16">
        <div className="max-w-5xl mx-auto px-6">
          <div className="flex flex-col md:flex-row items-center gap-8">
            <img 
              src={user.profilePhoto} 
              alt={user.name}
              className="w-40 h-40 rounded-full object-cover border-4 border-white shadow-lg"
            />
            <div className="text-center md:text-left">
              <h1 className="text-4xl font-bold mb-2">{user.name}</h1>
              <p className="text-xl text-gray-300 mb-4">{user.bio}</p>
              <div className="flex flex-wrap justify-center md:justify-start gap-4">
                {user.location && (
                  <div className="flex items-center text-gray-300">
                    <MapPin className="w-4 h-4 mr-2" />
                    {user.location}
                  </div>
                )}
                {user.email && (
                  <div className="flex items-center text-gray-300">
                    <Mail className="w-4 h-4 mr-2" />
                    {user.email}
                  </div>
                )}
                {user.phone && (
                  <div className="flex items-center text-gray-300">
                    <Phone className="w-4 h-4 mr-2" />
                    {user.phone}
                  </div>
                )}
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <div className="max-w-5xl mx-auto px-6 py-12">
        {/* Social Links & Resume */}
        <div className="flex flex-wrap justify-center gap-4 mb-12 pb-12 border-b">
          {user.socialLinks?.linkedin && (
            <a 
              href={user.socialLinks.linkedin} 
              target="_blank" 
              rel="noopener noreferrer"
              className="inline-flex items-center px-4 py-2 border border-gray-300 rounded hover:bg-gray-50 transition-colors"
            >
              <Linkedin className="w-4 h-4 mr-2" />
              LinkedIn
            </a>
          )}
          {user.socialLinks?.github && (
            <a 
              href={user.socialLinks.github} 
              target="_blank" 
              rel="noopener noreferrer"
              className="inline-flex items-center px-4 py-2 border border-gray-300 rounded hover:bg-gray-50 transition-colors"
            >
              <Github className="w-4 h-4 mr-2" />
              GitHub
            </a>
          )}
          {user.socialLinks?.twitter && (
            <a 
              href={user.socialLinks.twitter} 
              target="_blank" 
              rel="noopener noreferrer"
              className="inline-flex items-center px-4 py-2 border border-gray-300 rounded hover:bg-gray-50 transition-colors"
            >
              <Twitter className="w-4 h-4 mr-2" />
              Twitter
            </a>
          )}
          {user.socialLinks?.website && (
            <a 
              href={user.socialLinks.website} 
              target="_blank" 
              rel="noopener noreferrer"
              className="inline-flex items-center px-4 py-2 border border-gray-300 rounded hover:bg-gray-50 transition-colors"
            >
              <Globe className="w-4 h-4 mr-2" />
              Website
            </a>
          )}
          {user.resumeUrl && (
            <button className="inline-flex items-center px-6 py-2 bg-gray-900 text-white rounded hover:bg-gray-800 transition-colors">
              <Download className="w-4 h-4 mr-2" />
              Download Resume
            </button>
          )}
        </div>

        {/* Skills Section */}
        {skills.length > 0 && (
          <section className="mb-16">
            <div className="flex items-center mb-6">
              <div className="w-1 h-8 bg-gray-900 mr-4"></div>
              <h2 className="text-3xl font-bold text-gray-900">Professional Skills</h2>
            </div>
            <div className="bg-gray-50 p-8 rounded-lg">
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {skills.map((skill) => (
                  <div key={skill.id}>
                    <div className="flex justify-between mb-2">
                      <span className="font-semibold text-gray-900">{skill.name}</span>
                      <span className="text-gray-600">{skill.level}%</span>
                    </div>
                    <div className="w-full bg-gray-200 rounded-full h-3">
                      <div 
                        className="bg-gray-900 h-3 rounded-full transition-all"
                        style={{ width: `${skill.level}%` }}
                      />
                    </div>
                    <div className="text-xs text-gray-500 mt-1">{skill.category}</div>
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}

        {/* Projects Section */}
        {projects.length > 0 && (
          <section className="mb-16">
            <div className="flex items-center mb-6">
              <div className="w-1 h-8 bg-gray-900 mr-4"></div>
              <h2 className="text-3xl font-bold text-gray-900">Portfolio</h2>
            </div>
            <div className="space-y-8">
              {projects.map((project, index) => (
                <div key={project.id} className="border border-gray-200 rounded-lg overflow-hidden">
                  {project.image && (
                    <img 
                      src={project.image} 
                      alt={project.title}
                      className="w-full h-64 object-cover"
                    />
                  )}
                  <div className="p-6">
                    <div className="flex items-start justify-between mb-3">
                      <h3 className="text-2xl font-bold text-gray-900">{project.title}</h3>
                      {project.featured && (
                        <span className="bg-gray-900 text-white text-xs px-3 py-1 rounded">Featured</span>
                      )}
                    </div>
                    <p className="text-gray-700 mb-4 leading-relaxed">{project.description}</p>
                    {project.techStack && project.techStack.length > 0 && (
                      <div className="flex flex-wrap gap-2 mb-4">
                        {project.techStack.map((tech, idx) => (
                          <span key={idx} className="bg-gray-100 text-gray-700 text-sm px-3 py-1 rounded">
                            {tech}
                          </span>
                        ))}
                      </div>
                    )}
                    <div className="flex space-x-4">
                      {project.demoLink && (
                        <a 
                          href={project.demoLink} 
                          target="_blank" 
                          rel="noopener noreferrer"
                          className="inline-flex items-center text-gray-900 hover:text-gray-700 font-medium"
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
                          className="inline-flex items-center text-gray-900 hover:text-gray-700 font-medium"
                        >
                          <Github className="w-4 h-4 mr-1" />
                          Source Code
                        </a>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {/* Achievements Section */}
        {achievements.length > 0 && (
          <section className="mb-16">
            <div className="flex items-center mb-6">
              <div className="w-1 h-8 bg-gray-900 mr-4"></div>
              <h2 className="text-3xl font-bold text-gray-900">Achievements & Certifications</h2>
            </div>
            <div className="bg-gray-50 p-8 rounded-lg">
              <div className="space-y-6">
                {achievements.map((achievement) => (
                  <div key={achievement.id} className="flex items-start space-x-4">
                    <div className="bg-gray-900 p-3 rounded-full flex-shrink-0">
                      <Award className="w-5 h-5 text-white" />
                    </div>
                    <div className="flex-1">
                      <h3 className="text-xl font-bold text-gray-900 mb-1">{achievement.title}</h3>
                      <p className="text-gray-600 mb-2">{achievement.issuer} • {achievement.date}</p>
                      {achievement.description && (
                        <p className="text-gray-700">{achievement.description}</p>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}
      </div>

      {/* Footer */}
      <footer className="bg-gray-900 text-white py-8">
        <div className="max-w-5xl mx-auto px-6 text-center">
          <p>&copy; 2025 {user.name}. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
};

export default ProfessionalTemplate;