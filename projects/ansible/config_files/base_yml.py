# Copyright (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
base_yaml="""
---
ALLOW_WORLD_READABLE_TMPFILES:
  name: Allow world-readable temporary files
  deprecated:
    why: moved to a per plugin approach that is more flexible
    version: "2.14"
    alternatives: mostly the same config will work, but now controlled from the plugin itself and not using the general constant.
  default: False
  description:
    - This makes the temporary files created on the machine world-readable and will issue a warning instead of failing the task.
    - It is useful when becoming an unprivileged user.
  env: []
  ini:
  - {key: allow_world_readable_tmpfiles, section: defaults}
  type: boolean
  yaml: {key: defaults.allow_world_readable_tmpfiles}
  version_added: "2.1"
ANSIBLE_CONNECTION_PATH:
  name: Path of ansible-connection script
  default: null
  description:
    - Specify where to look for the ansible-connection script. This location will be checked before searching $PATH.
    - If null, ansible will start with the same directory as the ansible script.
  type: path
  env: [{name: ANSIBLE_CONNECTION_PATH}]
  ini:
  - {key: ansible_connection_path, section: persistent_connection}
  yaml: {key: persistent_connection.ansible_connection_path}
  version_added: "2.8"
ANSIBLE_COW_SELECTION:
  name: Cowsay filter selection
  default: default
  description: This allows you to chose a specific cowsay stencil for the banners or use 'random' to cycle through them.
  env: [{name: ANSIBLE_COW_SELECTION}]
  ini:
  - {key: cow_selection, section: defaults}
ANSIBLE_COW_ACCEPTLIST:
  name: Cowsay filter acceptance list
  default: ['bud-frogs', 'bunny', 'cheese', 'daemon', 'default', 'dragon', 'elephant-in-snake', 'elephant', 'eyes', 'hellokitty', 'kitty', 'luke-koala', 'meow', 'milk', 'moofasa', 'moose', 'ren', 'sheep', 'small', 'stegosaurus', 'stimpy', 'supermilker', 'three-eyes', 'turkey', 'turtle', 'tux', 'udder', 'vader-koala', 'vader', 'www']
  description: White list of cowsay templates that are 'safe' to use, set to empty list if you want to enable all installed templates.
  env:
  - name: ANSIBLE_COW_WHITELIST
    deprecated:
      why: normalizing names to new standard
      version: "2.15"
      alternatives: 'ANSIBLE_COW_ACCEPTLIST'
  - name: ANSIBLE_COW_ACCEPTLIST
    version_added: '2.11'
  ini:
  - key: cow_whitelist
    section: defaults
    deprecated:
      why: normalizing names to new standard
      version: "2.15"
      alternatives: 'cowsay_enabled_stencils'
  - key: cowsay_enabled_stencils
    section: defaults
    version_added: '2.11'
  type: list
ANSIBLE_FORCE_COLOR:
  name: Force color output
  default: False
  description: This option forces color mode even when running without a TTY or the "nocolor" setting is True.
  env: [{name: ANSIBLE_FORCE_COLOR}]
  ini:
  - {key: force_color, section: defaults}
  type: boolean
  yaml: {key: display.force_color}
ANSIBLE_NOCOLOR:
  name: Suppress color output
  default: False
  description: This setting allows suppressing colorizing output, which is used to give a better indication of failure and status information.
  env:
    - name: ANSIBLE_NOCOLOR
      # this is generic convention for CLI programs
    - name: NO_COLOR
      version_added: '2.11'
  ini:
  - {key: nocolor, section: defaults}
  type: boolean
  yaml: {key: display.nocolor}
ANSIBLE_NOCOWS:
  name: Suppress cowsay output
  default: False
  description: If you have cowsay installed but want to avoid the 'cows' (why????), use this.
  env: [{name: ANSIBLE_NOCOWS}]
  ini:
  - {key: nocows, section: defaults}
  type: boolean
  yaml: {key: display.i_am_no_fun}
ANSIBLE_COW_PATH:
  name: Set path to cowsay command
  default: null
  description: Specify a custom cowsay path or swap in your cowsay implementation of choice
  env: [{name: ANSIBLE_COW_PATH}]
  ini:
  - {key: cowpath, section: defaults}
  type: string
  yaml: {key: display.cowpath}
ANSIBLE_PIPELINING:
  name: Connection pipelining
  default: False
  description:
    - Pipelining, if supported by the connection plugin, reduces the number of network operations required to execute a module on the remote server,
      by executing many Ansible modules without actual file transfer.
    - This can result in a very significant performance improvement when enabled.
    - "However this conflicts with privilege escalation (become). For example, when using 'sudo:' operations you must first
      disable 'requiretty' in /etc/sudoers on all managed hosts, which is why it is disabled by default."
    - This option is disabled if ``ANSIBLE_KEEP_REMOTE_FILES`` is enabled.
  env:
    - name: ANSIBLE_PIPELINING
    - name: ANSIBLE_SSH_PIPELINING
  ini:
  - section: connection
    key: pipelining
  - section: ssh_connection
    key: pipelining
  type: boolean
  yaml: {key: plugins.connection.pipelining}
ANSIBLE_SSH_ARGS:
  # TODO: move to ssh plugin
  default: -C -o ControlMaster=auto -o ControlPersist=60s
  description:
    - If set, this will override the Ansible default ssh arguments.
    - In particular, users may wish to raise the ControlPersist time to encourage performance.  A value of 30 minutes may be appropriate.
    - Be aware that if `-o ControlPath` is set in ssh_args, the control path setting is not used.
  env: [{name: ANSIBLE_SSH_ARGS}]
  ini:
  - {key: ssh_args, section: ssh_connection}
  yaml: {key: ssh_connection.ssh_args}
ANSIBLE_SSH_CONTROL_PATH:
  # TODO: move to ssh plugin
  default: null
  description:
    - This is the location to save ssh's ControlPath sockets, it uses ssh's variable substitution.
    - Since 2.3, if null, ansible will generate a unique hash. Use `%(directory)s` to indicate where to use the control dir path setting.
    - Before 2.3 it defaulted to `control_path=%(directory)s/ansible-ssh-%%h-%%p-%%r`.
    - Be aware that this setting is ignored if `-o ControlPath` is set in ssh args.
  env: [{name: ANSIBLE_SSH_CONTROL_PATH}]
  ini:
  - {key: control_path, section: ssh_connection}
  yaml: {key: ssh_connection.control_path}
ANSIBLE_SSH_CONTROL_PATH_DIR:
  # TODO: move to ssh plugin
  default: ~/.ansible/cp
  description:
    - This sets the directory to use for ssh control path if the control path setting is null.
    - Also, provides the `%(directory)s` variable for the control path setting.
  env: [{name: ANSIBLE_SSH_CONTROL_PATH_DIR}]
  ini:
  - {key: control_path_dir, section: ssh_connection}
  yaml: {key: ssh_connection.control_path_dir}
ANSIBLE_SSH_EXECUTABLE:
  # TODO: move to ssh plugin, note that ssh_utils  refs this and needs to be updated if removed
  default: ssh
  description:
    - This defines the location of the ssh binary. It defaults to `ssh` which will use the first ssh binary available in $PATH.
    - This option is usually not required, it might be useful when access to system ssh is restricted,
      or when using ssh wrappers to connect to remote hosts.
  env: [{name: ANSIBLE_SSH_EXECUTABLE}]
  ini:
  - {key: ssh_executable, section: ssh_connection}
  yaml: {key: ssh_connection.ssh_executable}
  version_added: "2.2"
ANSIBLE_SSH_RETRIES:
  # TODO: move to ssh plugin
  default: 0
  description: Number of attempts to establish a connection before we give up and report the host as 'UNREACHABLE'
  env: [{name: ANSIBLE_SSH_RETRIES}]
  ini:
  - {key: retries, section: ssh_connection}
  type: integer
  yaml: {key: ssh_connection.retries}
ANY_ERRORS_FATAL:
  name: Make Task failures fatal
  default: False
  description: Sets the default value for the any_errors_fatal keyword, if True, Task failures will be considered fatal errors.
  env:
    - name: ANSIBLE_ANY_ERRORS_FATAL
  ini:
    - section:  defaults
      key: any_errors_fatal
  type: boolean
  yaml: {key: errors.any_task_errors_fatal}
  version_added: "2.4"
BECOME_ALLOW_SAME_USER:
  name: Allow becoming the same user
  default: False
  description: This setting controls if become is skipped when remote user and become user are the same. I.E root sudo to root.
  env: [{name: ANSIBLE_BECOME_ALLOW_SAME_USER}]
  ini:
  - {key: become_allow_same_user, section: privilege_escalation}
  type: boolean
  yaml: {key: privilege_escalation.become_allow_same_user}
AGNOSTIC_BECOME_PROMPT:
  name: Display an agnostic become prompt
  default: True
  type: boolean
  description: Display an agnostic become prompt instead of displaying a prompt containing the command line supplied become method
  env: [{name: ANSIBLE_AGNOSTIC_BECOME_PROMPT}]
  ini:
    - {key: agnostic_become_prompt, section: privilege_escalation}
  yaml: {key: privilege_escalation.agnostic_become_prompt}
  version_added: "2.5"
CACHE_PLUGIN:
  name: Persistent Cache plugin
  default: memory
  description: Chooses which cache plugin to use, the default 'memory' is ephemeral.
  env: [{name: ANSIBLE_CACHE_PLUGIN}]
  ini:
  - {key: fact_caching, section: defaults}
  yaml: {key: facts.cache.plugin}
CACHE_PLUGIN_CONNECTION:
  name: Cache Plugin URI
  default: ~
  description: Defines connection or path information for the cache plugin
  env: [{name: ANSIBLE_CACHE_PLUGIN_CONNECTION}]
  ini:
  - {key: fact_caching_connection, section: defaults}
  yaml: {key: facts.cache.uri}
CACHE_PLUGIN_PREFIX:
  name: Cache Plugin table prefix
  default: ansible_facts
  description: Prefix to use for cache plugin files/tables
  env: [{name: ANSIBLE_CACHE_PLUGIN_PREFIX}]
  ini:
  - {key: fact_caching_prefix, section: defaults}
  yaml: {key: facts.cache.prefix}
CACHE_PLUGIN_TIMEOUT:
  name: Cache Plugin expiration timeout
  default: 86400
  description: Expiration timeout for the cache plugin data
  env: [{name: ANSIBLE_CACHE_PLUGIN_TIMEOUT}]
  ini:
  - {key: fact_caching_timeout, section: defaults}
  type: integer
  yaml: {key: facts.cache.timeout}
COLLECTIONS_SCAN_SYS_PATH:
  name: enable/disable scanning sys.path for installed collections
  default: true
  type: boolean
  env:
  - {name: ANSIBLE_COLLECTIONS_SCAN_SYS_PATH}
  ini:
  - {key: collections_scan_sys_path, section: defaults}
COLLECTIONS_PATHS:
  name: ordered list of root paths for loading installed Ansible collections content
  description: >
    Colon separated paths in which Ansible will search for collections content.
    Collections must be in nested *subdirectories*, not directly in these directories.
    For example, if ``COLLECTIONS_PATHS`` includes ``~/.ansible/collections``,
    and you want to add ``my.collection`` to that directory, it must be saved as
    ``~/.ansible/collections/ansible_collections/my/collection``.
  default: ~/.ansible/collections:/usr/share/ansible/collections
  type: pathspec
  env:
  - name: ANSIBLE_COLLECTIONS_PATHS  # TODO: Deprecate this and ini once PATH has been in a few releases.
  - name: ANSIBLE_COLLECTIONS_PATH
    version_added: '2.10'
  ini:
  - key: collections_paths
    section: defaults
  - key: collections_path
    section: defaults
    version_added: '2.10'
COLLECTIONS_ON_ANSIBLE_VERSION_MISMATCH:
  name: Defines behavior when loading a collection that does not support the current Ansible version
  description:
  - When a collection is loaded that does not support the running Ansible version (via the collection metadata key
    `requires_ansible`), the default behavior is to issue a warning and continue anyway. Setting this value to `ignore`
    skips the warning entirely, while setting it to `fatal` will immediately halt Ansible execution.
  env: [{name: ANSIBLE_COLLECTIONS_ON_ANSIBLE_VERSION_MISMATCH}]
  ini: [{key: collections_on_ansible_version_mismatch, section: defaults}]
  choices: [error, warning, ignore]
  default: warning
_COLOR_DEFAULTS: &color
  name: placeholder for color settings' defaults
  choices: ['black', 'bright gray', 'blue', 'white', 'green', 'bright blue', 'cyan', 'bright green', 'red', 'bright cyan', 'purple', 'bright red', 'yellow', 'bright purple', 'dark gray', 'bright yellow', 'magenta', 'bright magenta', 'normal']
COLOR_CHANGED:
  <<: *color
  name: Color for 'changed' task status
  default: yellow
  description: Defines the color to use on 'Changed' task status
  env: [{name: ANSIBLE_COLOR_CHANGED}]
  ini:
  - {key: changed, section: colors}
COLOR_CONSOLE_PROMPT:
  <<: *color
  name: "Color for ansible-console's prompt task status"
  default: white
  description: Defines the default color to use for ansible-console
  env: [{name: ANSIBLE_COLOR_CONSOLE_PROMPT}]
  ini:
  - {key: console_prompt, section: colors}
  version_added: "2.7"
COLOR_DEBUG:
  <<: *color
  name: Color for debug statements
  default: dark gray
  description: Defines the color to use when emitting debug messages
  env: [{name: ANSIBLE_COLOR_DEBUG}]
  ini:
  - {key: debug, section: colors}
COLOR_DEPRECATE:
  <<: *color
  name: Color for deprecation messages
  default: purple
  description: Defines the color to use when emitting deprecation messages
  env: [{name: ANSIBLE_COLOR_DEPRECATE}]
  ini:
  - {key: deprecate, section: colors}
COLOR_DIFF_ADD:
  <<: *color
  name: Color for diff added display
  default: green
  description: Defines the color to use when showing added lines in diffs
  env: [{name: ANSIBLE_COLOR_DIFF_ADD}]
  ini:
  - {key: diff_add, section: colors}
  yaml: {key: display.colors.diff.add}
COLOR_DIFF_LINES:
  <<: *color
  name: Color for diff lines display
  default: cyan
  description: Defines the color to use when showing diffs
  env: [{name: ANSIBLE_COLOR_DIFF_LINES}]
  ini:
  - {key: diff_lines, section: colors}
COLOR_DIFF_REMOVE:
  <<: *color
  name: Color for diff removed display
  default: red
  description: Defines the color to use when showing removed lines in diffs
  env: [{name: ANSIBLE_COLOR_DIFF_REMOVE}]
  ini:
  - {key: diff_remove, section: colors}
COLOR_ERROR:
  <<: *color
  name: Color for error messages
  default: red
  description: Defines the color to use when emitting error messages
  env: [{name: ANSIBLE_COLOR_ERROR}]
  ini:
  - {key: error, section: colors}
  yaml: {key: colors.error}
COLOR_HIGHLIGHT:
  <<: *color
  name: Color for highlighting
  default: white
  description: Defines the color to use for highlighting
  env: [{name: ANSIBLE_COLOR_HIGHLIGHT}]
  ini:
  - {key: highlight, section: colors}
COLOR_OK:
  <<: *color
  name: Color for 'ok' task status
  default: green
  description: Defines the color to use when showing 'OK' task status
  env: [{name: ANSIBLE_COLOR_OK}]
  ini:
  - {key: ok, section: colors}
COLOR_SKIP:
  <<: *color
  name: Color for 'skip' task status
  default: cyan
  description: Defines the color to use when showing 'Skipped' task status
  env: [{name: ANSIBLE_COLOR_SKIP}]
  ini:
  - {key: skip, section: colors}
COLOR_UNREACHABLE:
  <<: *color
  name: Color for 'unreachable' host state
  default: bright red
  description: Defines the color to use on 'Unreachable' status
  env: [{name: ANSIBLE_COLOR_UNREACHABLE}]
  ini:
  - {key: unreachable, section: colors}
COLOR_VERBOSE:
  <<: *color
  name: Color for verbose messages
  default: blue
  description: Defines the color to use when emitting verbose messages. i.e those that show with '-v's.
  env: [{name: ANSIBLE_COLOR_VERBOSE}]
  ini:
  - {key: verbose, section: colors}
COLOR_WARN:
  <<: *color
  name: Color for warning messages
  default: bright purple
  description: Defines the color to use when emitting warning messages
  env: [{name: ANSIBLE_COLOR_WARN}]
  ini:
  - {key: warn, section: colors}
CONDITIONAL_BARE_VARS:
  name: Allow bare variable evaluation in conditionals
  default: False
  type: boolean
  description:
    - With this setting on (True), running conditional evaluation 'var' is treated differently than 'var.subkey' as the first is evaluated
      directly while the second goes through the Jinja2 parser. But 'false' strings in 'var' get evaluated as booleans.
    - With this setting off they both evaluate the same but in cases in which 'var' was 'false' (a string) it won't get evaluated as a boolean anymore.
    - Currently this setting defaults to 'True' but will soon change to 'False' and the setting itself will be removed in the future.
    - Expect that this setting eventually will be deprecated after 2.12
  env: [{name: ANSIBLE_CONDITIONAL_BARE_VARS}]
  ini:
  - {key: conditional_bare_variables, section: defaults}
  version_added: "2.8"
COVERAGE_REMOTE_OUTPUT:
  name: Sets the output directory and filename prefix to generate coverage run info.
  description:
    - Sets the output directory on the remote host to generate coverage reports to.
    - Currently only used for remote coverage on PowerShell modules.
    - This is for internal use only.
  env:
  - {name: _ANSIBLE_COVERAGE_REMOTE_OUTPUT}
  vars:
  - {name: _ansible_coverage_remote_output}
  type: str
  version_added: '2.9'
COVERAGE_REMOTE_PATHS:
  name: Sets the list of paths to run coverage for.
  description:
  - A list of paths for files on the Ansible controller to run coverage for when executing on the remote host.
  - Only files that match the path glob will have its coverage collected.
  - Multiple path globs can be specified and are separated by ``:``.
  - Currently only used for remote coverage on PowerShell modules.
  - This is for internal use only.
  default: '*'
  env:
  - {name: _ANSIBLE_COVERAGE_REMOTE_PATH_FILTER}
  type: str
  version_added: '2.9'
ACTION_WARNINGS:
  name: Toggle action warnings
  default: True
  description:
    - By default Ansible will issue a warning when received from a task action (module or action plugin)
    - These warnings can be silenced by adjusting this setting to False.
  env: [{name: ANSIBLE_ACTION_WARNINGS}]
  ini:
  - {key: action_warnings, section: defaults}
  type: boolean
  version_added: "2.5"
COMMAND_WARNINGS:
  name: Command module warnings
  default: False
  description:
    - Ansible can issue a warning when the shell or command module is used and the command appears to be similar to an existing Ansible module.
    - These warnings can be silenced by adjusting this setting to False. You can also control this at the task level with the module option ``warn``.
    - As of version 2.11, this is disabled by default.
  env: [{name: ANSIBLE_COMMAND_WARNINGS}]
  ini:
  - {key: command_warnings, section: defaults}
  type: boolean
  version_added: "1.8"
  deprecated:
    why: the command warnings feature is being removed
    version: "2.14"
LOCALHOST_WARNING:
  name: Warning when using implicit inventory with only localhost
  default: True
  description:
    - By default Ansible will issue a warning when there are no hosts in the
      inventory.
    - These warnings can be silenced by adjusting this setting to False.
  env: [{name: ANSIBLE_LOCALHOST_WARNING}]
  ini:
  - {key: localhost_warning, section: defaults}
  type: boolean
  version_added: "2.6"
DOC_FRAGMENT_PLUGIN_PATH:
  name: documentation fragment plugins path
  default: ~/.ansible/plugins/doc_fragments:/usr/share/ansible/plugins/doc_fragments
  description: Colon separated paths in which Ansible will search for Documentation Fragments Plugins.
  env: [{name: ANSIBLE_DOC_FRAGMENT_PLUGINS}]
  ini:
  - {key: doc_fragment_plugins, section: defaults}
  type: pathspec
DEFAULT_ACTION_PLUGIN_PATH:
  name: Action plugins path
  default: ~/.ansible/plugins/action:/usr/share/ansible/plugins/action
  description: Colon separated paths in which Ansible will search for Action Plugins.
  env: [{name: ANSIBLE_ACTION_PLUGINS}]
  ini:
  - {key: action_plugins, section: defaults}
  type: pathspec
  yaml: {key: plugins.action.path}
DEFAULT_ALLOW_UNSAFE_LOOKUPS:
  name: Allow unsafe lookups
  default: False
  description:
    - "When enabled, this option allows lookup plugins (whether used in variables as ``{{lookup('foo')}}`` or as a loop as with_foo)
      to return data that is not marked 'unsafe'."
    - By default, such data is marked as unsafe to prevent the templating engine from evaluating any jinja2 templating language,
      as this could represent a security risk.  This option is provided to allow for backwards-compatibility,
      however users should first consider adding allow_unsafe=True to any lookups which may be expected to contain data which may be run
      through the templating engine late
  env: []
  ini:
  - {key: allow_unsafe_lookups, section: defaults}
  type: boolean
  version_added: "2.2.3"
DEFAULT_ASK_PASS:
  name: Ask for the login password
  default: False
  description:
    - This controls whether an Ansible playbook should prompt for a login password.
      If using SSH keys for authentication, you probably do not needed to change this setting.
  env: [{name: ANSIBLE_ASK_PASS}]
  ini:
  - {key: ask_pass, section: defaults}
  type: boolean
  yaml: {key: defaults.ask_pass}
DEFAULT_ASK_VAULT_PASS:
  name: Ask for the vault password(s)
  default: False
  description:
    - This controls whether an Ansible playbook should prompt for a vault password.
  env: [{name: ANSIBLE_ASK_VAULT_PASS}]
  ini:
  - {key: ask_vault_pass, section: defaults}
  type: boolean
DEFAULT_BECOME:
  name: Enable privilege escalation (become)
  default: False
  description: Toggles the use of privilege escalation, allowing you to 'become' another user after login.
  env: [{name: ANSIBLE_BECOME}]
  ini:
  - {key: become, section: privilege_escalation}
  type: boolean
DEFAULT_BECOME_ASK_PASS:
  name: Ask for the privilege escalation (become) password
  default: False
  description: Toggle to prompt for privilege escalation password.
  env: [{name: ANSIBLE_BECOME_ASK_PASS}]
  ini:
  - {key: become_ask_pass, section: privilege_escalation}
  type: boolean
DEFAULT_BECOME_METHOD:
  name: Choose privilege escalation method
  default: 'sudo'
  description: Privilege escalation method to use when `become` is enabled.
  env: [{name: ANSIBLE_BECOME_METHOD}]
  ini:
    - {section: privilege_escalation, key: become_method}
DEFAULT_BECOME_EXE:
  name: Choose 'become' executable
  default: ~
  description: 'executable to use for privilege escalation, otherwise Ansible will depend on PATH'
  env: [{name: ANSIBLE_BECOME_EXE}]
  ini:
  - {key: become_exe, section: privilege_escalation}
DEFAULT_BECOME_FLAGS:
  name: Set 'become' executable options
  default: ''
  description: Flags to pass to the privilege escalation executable.
  env: [{name: ANSIBLE_BECOME_FLAGS}]
  ini:
  - {key: become_flags, section: privilege_escalation}
BECOME_PLUGIN_PATH:
  name: Become plugins path
  default: ~/.ansible/plugins/become:/usr/share/ansible/plugins/become
  description: Colon separated paths in which Ansible will search for Become Plugins.
  env: [{name: ANSIBLE_BECOME_PLUGINS}]
  ini:
  - {key: become_plugins, section: defaults}
  type: pathspec
  version_added: "2.8"
DEFAULT_BECOME_USER:
  # FIXME: should really be blank and make -u passing optional depending on it
  name: Set the user you 'become' via privilege escalation
  default: root
  description: The user your login/remote user 'becomes' when using privilege escalation, most systems will use 'root' when no user is specified.
  env: [{name: ANSIBLE_BECOME_USER}]
  ini:
  - {key: become_user, section: privilege_escalation}
  yaml: {key: become.user}
DEFAULT_CACHE_PLUGIN_PATH:
  name: Cache Plugins Path
  default: ~/.ansible/plugins/cache:/usr/share/ansible/plugins/cache
  description: Colon separated paths in which Ansible will search for Cache Plugins.
  env: [{name: ANSIBLE_CACHE_PLUGINS}]
  ini:
  - {key: cache_plugins, section: defaults}
  type: pathspec
CALLABLE_ACCEPT_LIST:
  name: Template 'callable' accept list
  default: []
  description: Whitelist of callable methods to be made available to template evaluation
  env:
  - name: ANSIBLE_CALLABLE_WHITELIST
    deprecated:
      why: normalizing names to new standard
      version: "2.15"
      alternatives: 'ANSIBLE_CALLABLE_ENABLED'
  - name: ANSIBLE_CALLABLE_ENABLED
    version_added: '2.11'
  ini:
  - key: callable_whitelist
    section: defaults
    deprecated:
      why: normalizing names to new standard
      version: "2.15"
      alternatives: 'callable_enabled'
  - key: callable_enabled
    section: defaults
    version_added: '2.11'
  type: list
CONTROLLER_PYTHON_WARNING:
  name: Running Older than Python 3.8 Warning
  default: True
  description: Toggle to control showing warnings related to running a Python version
               older than Python 3.8 on the controller
  env: [{name: ANSIBLE_CONTROLLER_PYTHON_WARNING}]
  ini:
  - {key: controller_python_warning, section: defaults}
  type: boolean
DEFAULT_CALLBACK_PLUGIN_PATH:
  name: Callback Plugins Path
  default: ~/.ansible/plugins/callback:/usr/share/ansible/plugins/callback
  description: Colon separated paths in which Ansible will search for Callback Plugins.
  env: [{name: ANSIBLE_CALLBACK_PLUGINS}]
  ini:
  - {key: callback_plugins, section: defaults}
  type: pathspec
  yaml: {key: plugins.callback.path}
CALLBACKS_ENABLED:
  name: Enable callback plugins that require it.
  default: []
  description:
    - "List of enabled callbacks, not all callbacks need enabling,
      but many of those shipped with Ansible do as we don't want them activated by default."
  env:
  - name: ANSIBLE_CALLBACK_WHITELIST
    deprecated:
      why: normalizing names to new standard
      version: "2.15"
      alternatives: 'ANSIBLE_CALLBACKS_ENABLED'
  - name: ANSIBLE_CALLBACKS_ENABLED
    version_added: '2.11'
  ini:
  - key: callback_whitelist
    section: defaults
    deprecated:
      why: normalizing names to new standard
      version: "2.15"
      alternatives: 'callback_enabled'
  - key: callbacks_enabled
    section: defaults
    version_added: '2.11'
  type: list
DEFAULT_CLICONF_PLUGIN_PATH:
  name: Cliconf Plugins Path
  default: ~/.ansible/plugins/cliconf:/usr/share/ansible/plugins/cliconf
  description: Colon separated paths in which Ansible will search for Cliconf Plugins.
  env: [{name: ANSIBLE_CLICONF_PLUGINS}]
  ini:
  - {key: cliconf_plugins, section: defaults}
  type: pathspec
DEFAULT_CONNECTION_PLUGIN_PATH:
  name: Connection Plugins Path
  default: ~/.ansible/plugins/connection:/usr/share/ansible/plugins/connection
  description: Colon separated paths in which Ansible will search for Connection Plugins.
  env: [{name: ANSIBLE_CONNECTION_PLUGINS}]
  ini:
  - {key: connection_plugins, section: defaults}
  type: pathspec
  yaml: {key: plugins.connection.path}
DEFAULT_DEBUG:
  name: Debug mode
  default: False
  description:
    - "Toggles debug output in Ansible. This is *very* verbose and can hinder
      multiprocessing.  Debug output can also include secret information
      despite no_log settings being enabled, which means debug mode should not be used in
      production."
  env: [{name: ANSIBLE_DEBUG}]
  ini:
  - {key: debug, section: defaults}
  type: boolean
DEFAULT_EXECUTABLE:
  name: Target shell executable
  default: /bin/sh
  description:
    - "This indicates the command to use to spawn a shell under for Ansible's execution needs on a target.
      Users may need to change this in rare instances when shell usage is constrained, but in most cases it may be left as is."
  env: [{name: ANSIBLE_EXECUTABLE}]
  ini:
  - {key: executable, section: defaults}
DEFAULT_FACT_PATH:
  name: local fact path
  default: ~
  description:
    - "This option allows you to globally configure a custom path for 'local_facts' for the implied M(ansible.builtin.setup) task when using fact gathering."
    - "If not set, it will fallback to the default from the M(ansible.builtin.setup) module: ``/etc/ansible/facts.d``."
    - "This does **not** affect  user defined tasks that use the M(ansible.builtin.setup) module."
  env: [{name: ANSIBLE_FACT_PATH}]
  ini:
  - {key: fact_path, section: defaults}
  type: string
  yaml: {key: facts.gathering.fact_path}
DEFAULT_FILTER_PLUGIN_PATH:
  name: Jinja2 Filter Plugins Path
  default: ~/.ansible/plugins/filter:/usr/share/ansible/plugins/filter
  description: Colon separated paths in which Ansible will search for Jinja2 Filter Plugins.
  env: [{name: ANSIBLE_FILTER_PLUGINS}]
  ini:
  - {key: filter_plugins, section: defaults}
  type: pathspec
DEFAULT_FORCE_HANDLERS:
  name: Force handlers to run after failure
  default: False
  description:
    - This option controls if notified handlers run on a host even if a failure occurs on that host.
    - When false, the handlers will not run if a failure has occurred on a host.
    - This can also be set per play or on the command line. See Handlers and Failure for more details.
  env: [{name: ANSIBLE_FORCE_HANDLERS}]
  ini:
  - {key: force_handlers, section: defaults}
  type: boolean
  version_added: "1.9.1"
DEFAULT_FORKS:
  name: Number of task forks
  default: 5
  description: Maximum number of forks Ansible will use to execute tasks on target hosts.
  env: [{name: ANSIBLE_FORKS}]
  ini:
  - {key: forks, section: defaults}
  type: integer
DEFAULT_GATHERING:
  name: Gathering behaviour
  default: 'implicit'
  description:
    - This setting controls the default policy of fact gathering (facts discovered about remote systems).
    - "When 'implicit' (the default), the cache plugin will be ignored and facts will be gathered per play unless 'gather_facts: False' is set."
    - "When 'explicit' the inverse is true, facts will not be gathered unless directly requested in the play."
    - "The 'smart' value means each new host that has no facts discovered will be scanned,
      but if the same host is addressed in multiple plays it will not be contacted again in the playbook run."
    - "This option can be useful for those wishing to save fact gathering time. Both 'smart' and 'explicit' will use the cache plugin."
  env: [{name: ANSIBLE_GATHERING}]
  ini:
    - key: gathering
      section: defaults
  version_added: "1.6"
  choices: ['smart', 'explicit', 'implicit']
DEFAULT_GATHER_SUBSET:
  name: Gather facts subset
  default: ['all']
  description:
      - Set the `gather_subset` option for the M(ansible.builtin.setup) task in the implicit fact gathering.
        See the module documentation for specifics.
      - "It does **not** apply to user defined M(ansible.builtin.setup) tasks."
  env: [{name: ANSIBLE_GATHER_SUBSET}]
  ini:
    - key: gather_subset
      section: defaults
  version_added: "2.1"
  type: list
DEFAULT_GATHER_TIMEOUT:
  name: Gather facts timeout
  default: 10
  description:
    - Set the timeout in seconds for the implicit fact gathering.
    - "It does **not** apply to user defined M(ansible.builtin.setup) tasks."
  env: [{name: ANSIBLE_GATHER_TIMEOUT}]
  ini:
  - {key: gather_timeout, section: defaults}
  type: integer
  yaml: {key: defaults.gather_timeout}
DEFAULT_HANDLER_INCLUDES_STATIC:
  name: Make handler M(ansible.builtin.include) static
  default: False
  description:
    - "Since 2.0 M(ansible.builtin.include) can be 'dynamic', this setting (if True) forces that if the include appears in a ``handlers`` section to be 'static'."
  env: [{name: ANSIBLE_HANDLER_INCLUDES_STATIC}]
  ini:
  - {key: handler_includes_static, section: defaults}
  type: boolean
  deprecated:
    why: include itself is deprecated and this setting will not matter in the future
    version: "2.12"
    alternatives: none as its already built into the decision between include_tasks and import_tasks
DEFAULT_HASH_BEHAVIOUR:
  name: Hash merge behaviour
  default: replace
  type: string
  choices: ["replace", "merge"]
  description:
    - This setting controls how variables merge in Ansible.
      By default Ansible will override variables in specific precedence orders, as described in Variables.
      When a variable of higher precedence wins, it will replace the other value.
    - "Some users prefer that variables that are hashes (aka 'dictionaries' in Python terms) are merged.
      This setting is called 'merge'. This is not the default behavior and it does not affect variables whose values are scalars
      (integers, strings) or arrays.  We generally recommend not using this setting unless you think you have an absolute need for it,
      and playbooks in the official examples repos do not use this setting"
    - In version 2.0 a ``combine`` filter was added to allow doing this for a particular variable (described in Filters).
  env: [{name: ANSIBLE_HASH_BEHAVIOUR}]
  ini:
  - {key: hash_behaviour, section: defaults}
  deprecated:
    why: this feature is fragile and not portable, leading to continual confusion and misuse
    version: "2.13"
    alternatives: the ``combine`` filter explicitly
DEFAULT_HOST_LIST:
  name: Inventory Source
  default: /etc/ansible/hosts
  description: Comma separated list of Ansible inventory sources
  env:
    - name: ANSIBLE_INVENTORY
  expand_relative_paths: True
  ini:
    - key: inventory
      section: defaults
  type: pathlist
  yaml: {key: defaults.inventory}
DEFAULT_HTTPAPI_PLUGIN_PATH:
  name: HttpApi Plugins Path
  default: ~/.ansible/plugins/httpapi:/usr/share/ansible/plugins/httpapi
  description: Colon separated paths in which Ansible will search for HttpApi Plugins.
  env: [{name: ANSIBLE_HTTPAPI_PLUGINS}]
  ini:
  - {key: httpapi_plugins, section: defaults}
  type: pathspec
DEFAULT_INTERNAL_POLL_INTERVAL:
  name: Internal poll interval
  default: 0.001
  env: []
  ini:
  - {key: internal_poll_interval, section: defaults}
  type: float
  version_added: "2.2"
  description:
    - This sets the interval (in seconds) of Ansible internal processes polling each other.
      Lower values improve performance with large playbooks at the expense of extra CPU load.
      Higher values are more suitable for Ansible usage in automation scenarios,
      when UI responsiveness is not required but CPU usage might be a concern.
    - "The default corresponds to the value hardcoded in Ansible <= 2.1"
DEFAULT_INVENTORY_PLUGIN_PATH:
  name: Inventory Plugins Path
  default: ~/.ansible/plugins/inventory:/usr/share/ansible/plugins/inventory
  description: Colon separated paths in which Ansible will search for Inventory Plugins.
  env: [{name: ANSIBLE_INVENTORY_PLUGINS}]
  ini:
  - {key: inventory_plugins, section: defaults}
  type: pathspec
DEFAULT_JINJA2_EXTENSIONS:
  name: Enabled Jinja2 extensions
  default: []
  description:
    - This is a developer-specific feature that allows enabling additional Jinja2 extensions.
    - "See the Jinja2 documentation for details. If you do not know what these do, you probably don't need to change this setting :)"
  env: [{name: ANSIBLE_JINJA2_EXTENSIONS}]
  ini:
  - {key: jinja2_extensions, section: defaults}
DEFAULT_JINJA2_NATIVE:
  name: Use Jinja2's NativeEnvironment for templating
  default: False
  description: This option preserves variable types during template operations. This requires Jinja2 >= 2.10.
  env: [{name: ANSIBLE_JINJA2_NATIVE}]
  ini:
  - {key: jinja2_native, section: defaults}
  type: boolean
  yaml: {key: jinja2_native}
  version_added: 2.7
DEFAULT_KEEP_REMOTE_FILES:
  name: Keep remote files
  default: False
  description:
    - Enables/disables the cleaning up of the temporary files Ansible used to execute the tasks on the remote.
    - If this option is enabled it will disable ``ANSIBLE_PIPELINING``.
  env: [{name: ANSIBLE_KEEP_REMOTE_FILES}]
  ini:
  - {key: keep_remote_files, section: defaults}
  type: boolean
DEFAULT_LIBVIRT_LXC_NOSECLABEL:
  # TODO: move to plugin
  name: No security label on Lxc
  default: False
  description:
    - "This setting causes libvirt to connect to lxc containers by passing --noseclabel to virsh.
      This is necessary when running on systems which do not have SELinux."
  env:
  - name: LIBVIRT_LXC_NOSECLABEL
    deprecated:
      why: environment variables without ``ANSIBLE_`` prefix are deprecated
      version: "2.12"
      alternatives: the ``ANSIBLE_LIBVIRT_LXC_NOSECLABEL`` environment variable
  - name: ANSIBLE_LIBVIRT_LXC_NOSECLABEL
  ini:
  - {key: libvirt_lxc_noseclabel, section: selinux}
  type: boolean
  version_added: "2.1"
DEFAULT_LOAD_CALLBACK_PLUGINS:
  name: Load callbacks for adhoc
  default: False
  description:
    - Controls whether callback plugins are loaded when running /usr/bin/ansible.
      This may be used to log activity from the command line, send notifications, and so on.
      Callback plugins are always loaded for ``ansible-playbook``.
  env: [{name: ANSIBLE_LOAD_CALLBACK_PLUGINS}]
  ini:
  - {key: bin_ansible_callbacks, section: defaults}
  type: boolean
  version_added: "1.8"
DEFAULT_LOCAL_TMP:
  name: Controller temporary directory
  default: ~/.ansible/tmp
  description: Temporary directory for Ansible to use on the controller.
  env: [{name: ANSIBLE_LOCAL_TEMP}]
  ini:
  - {key: local_tmp, section: defaults}
  type: tmppath
DEFAULT_LOG_PATH:
  name: Ansible log file path
  default: ~
  description: File to which Ansible will log on the controller. When empty logging is disabled.
  env: [{name: ANSIBLE_LOG_PATH}]
  ini:
  - {key: log_path, section: defaults}
  type: path
DEFAULT_LOG_FILTER:
  name: Name filters for python logger
  default: []
  description: List of logger names to filter out of the log file
  env: [{name: ANSIBLE_LOG_FILTER}]
  ini:
    - {key: log_filter, section: defaults}
  type: list
DEFAULT_LOOKUP_PLUGIN_PATH:
  name: Lookup Plugins Path
  description: Colon separated paths in which Ansible will search for Lookup Plugins.
  default: ~/.ansible/plugins/lookup:/usr/share/ansible/plugins/lookup
  env: [{name: ANSIBLE_LOOKUP_PLUGINS}]
  ini:
  - {key: lookup_plugins, section: defaults}
  type: pathspec
  yaml: {key: defaults.lookup_plugins}
DEFAULT_MANAGED_STR:
  name: Ansible managed
  default: 'Ansible managed'
  description: Sets the macro for the 'ansible_managed' variable available for M(ansible.builtin.template) and M(ansible.windows.win_template) modules.  This is only relevant for those two modules.
  env: []
  ini:
  - {key: ansible_managed, section: defaults}
  yaml: {key: defaults.ansible_managed}
DEFAULT_MODULE_ARGS:
  name: Adhoc default arguments
  default: ''
  description:
    - This sets the default arguments to pass to the ``ansible`` adhoc binary if no ``-a`` is specified.
  env: [{name: ANSIBLE_MODULE_ARGS}]
  ini:
  - {key: module_args, section: defaults}
DEFAULT_MODULE_COMPRESSION:
  name: Python module compression
  default: ZIP_DEFLATED
  description: Compression scheme to use when transferring Python modules to the target.
  env: []
  ini:
  - {key: module_compression, section: defaults}
# vars:
#   - name: ansible_module_compression
DEFAULT_MODULE_NAME:
  name: Default adhoc module
  default: command
  description: "Module to use with the ``ansible`` AdHoc command, if none is specified via ``-m``."
  env: []
  ini:
  - {key: module_name, section: defaults}
DEFAULT_MODULE_PATH:
  name: Modules Path
  description: Colon separated paths in which Ansible will search for Modules.
  default: ~/.ansible/plugins/modules:/usr/share/ansible/plugins/modules
  env: [{name: ANSIBLE_LIBRARY}]
  ini:
  - {key: library, section: defaults}
  type: pathspec
DEFAULT_MODULE_UTILS_PATH:
  name: Module Utils Path
  description: Colon separated paths in which Ansible will search for Module utils files, which are shared by modules.
  default: ~/.ansible/plugins/module_utils:/usr/share/ansible/plugins/module_utils
  env: [{name: ANSIBLE_MODULE_UTILS}]
  ini:
  - {key: module_utils, section: defaults}
  type: pathspec
DEFAULT_NETCONF_PLUGIN_PATH:
  name: Netconf Plugins Path
  default: ~/.ansible/plugins/netconf:/usr/share/ansible/plugins/netconf
  description: Colon separated paths in which Ansible will search for Netconf Plugins.
  env: [{name: ANSIBLE_NETCONF_PLUGINS}]
  ini:
  - {key: netconf_plugins, section: defaults}
  type: pathspec
DEFAULT_NO_LOG:
  name: No log
  default: False
  description: "Toggle Ansible's display and logging of task details, mainly used to avoid security disclosures."
  env: [{name: ANSIBLE_NO_LOG}]
  ini:
  - {key: no_log, section: defaults}
  type: boolean
DEFAULT_NO_TARGET_SYSLOG:
  name: No syslog on target
  default: False
  description:
  - Toggle Ansible logging to syslog on the target when it executes tasks. On Windows hosts this will disable a newer
    style PowerShell modules from writting to the event log.
  env: [{name: ANSIBLE_NO_TARGET_SYSLOG}]
  ini:
  - {key: no_target_syslog, section: defaults}
  vars:
  - name: ansible_no_target_syslog
    version_added: '2.10'
  type: boolean
  yaml: {key: defaults.no_target_syslog}
DEFAULT_NULL_REPRESENTATION:
  name: Represent a null
  default: ~
  description: What templating should return as a 'null' value. When not set it will let Jinja2 decide.
  env: [{name: ANSIBLE_NULL_REPRESENTATION}]
  ini:
  - {key: null_representation, section: defaults}
  type: none
DEFAULT_POLL_INTERVAL:
  name: Async poll interval
  default: 15
  description:
    - For asynchronous tasks in Ansible (covered in Asynchronous Actions and Polling),
      this is how often to check back on the status of those tasks when an explicit poll interval is not supplied.
      The default is a reasonably moderate 15 seconds which is a tradeoff between checking in frequently and
      providing a quick turnaround when something may have completed.
  env: [{name: ANSIBLE_POLL_INTERVAL}]
  ini:
  - {key: poll_interval, section: defaults}
  type: integer
DEFAULT_PRIVATE_KEY_FILE:
  name: Private key file
  default: ~
  description:
    - Option for connections using a certificate or key file to authenticate, rather than an agent or passwords,
      you can set the default value here to avoid re-specifying --private-key with every invocation.
  env: [{name: ANSIBLE_PRIVATE_KEY_FILE}]
  ini:
  - {key: private_key_file, section: defaults}
  type: path
DEFAULT_PRIVATE_ROLE_VARS:
  name: Private role variables
  default: False
  description:
    - Makes role variables inaccessible from other roles.
    - This was introduced as a way to reset role variables to default values if
      a role is used more than once in a playbook.
  env: [{name: ANSIBLE_PRIVATE_ROLE_VARS}]
  ini:
  - {key: private_role_vars, section: defaults}
  type: boolean
  yaml: {key: defaults.private_role_vars}
DEFAULT_REMOTE_PORT:
  name: Remote port
  default: ~
  description: Port to use in remote connections, when blank it will use the connection plugin default.
  env: [{name: ANSIBLE_REMOTE_PORT}]
  ini:
  - {key: remote_port, section: defaults}
  type: integer
  yaml: {key: defaults.remote_port}
DEFAULT_REMOTE_USER:
  name: Login/Remote User
  default:
  description:
    - Sets the login user for the target machines
    - "When blank it uses the connection plugin's default, normally the user currently executing Ansible."
  env: [{name: ANSIBLE_REMOTE_USER}]
  ini:
  - {key: remote_user, section: defaults}
DEFAULT_ROLES_PATH:
  name: Roles path
  default: ~/.ansible/roles:/usr/share/ansible/roles:/etc/ansible/roles
  description: Colon separated paths in which Ansible will search for Roles.
  env: [{name: ANSIBLE_ROLES_PATH}]
  expand_relative_paths: True
  ini:
  - {key: roles_path, section: defaults}
  type: pathspec
  yaml: {key: defaults.roles_path}
DEFAULT_SCP_IF_SSH:
  # TODO: move to ssh plugin
  default: smart
  description:
    - "Preferred method to use when transferring files over ssh."
    - When set to smart, Ansible will try them until one succeeds or they all fail.
    - If set to True, it will force 'scp', if False it will use 'sftp'.
  env: [{name: ANSIBLE_SCP_IF_SSH}]
  ini:
  - {key: scp_if_ssh, section: ssh_connection}
DEFAULT_SELINUX_SPECIAL_FS:
  name: Problematic file systems
  default: fuse, nfs, vboxsf, ramfs, 9p, vfat
  description:
    - "Some filesystems do not support safe operations and/or return inconsistent errors,
       this setting makes Ansible 'tolerate' those in the list w/o causing fatal errors."
    - Data corruption may occur and writes are not always verified when a filesystem is in the list.
  env:
  - name: ANSIBLE_SELINUX_SPECIAL_FS
    version_added: "2.9"
  ini:
  - {key: special_context_filesystems, section: selinux}
  type: list
DEFAULT_SFTP_BATCH_MODE:
  # TODO: move to ssh plugin
  default: True
  description: 'TODO: write it'
  env: [{name: ANSIBLE_SFTP_BATCH_MODE}]
  ini:
  - {key: sftp_batch_mode, section: ssh_connection}
  type: boolean
  yaml: {key: ssh_connection.sftp_batch_mode}
DEFAULT_SSH_TRANSFER_METHOD:
  # TODO: move to ssh plugin
  default:
  description: 'unused?'
  #  - "Preferred method to use when transferring files over ssh"
  #  - Setting to smart will try them until one succeeds or they all fail
  #choices: ['sftp', 'scp', 'dd', 'smart']
  env: [{name: ANSIBLE_SSH_TRANSFER_METHOD}]
  ini:
  - {key: transfer_method, section: ssh_connection}
DEFAULT_STDOUT_CALLBACK:
  name: Main display callback plugin
  default: default
  description:
    - "Set the main callback used to display Ansible output, you can only have one at a time."
    - You can have many other callbacks, but just one can be in charge of stdout.
  env: [{name: ANSIBLE_STDOUT_CALLBACK}]
  ini:
  - {key: stdout_callback, section: defaults}
ENABLE_TASK_DEBUGGER:
  name: Whether to enable the task debugger
  default: False
  description:
    - Whether or not to enable the task debugger, this previously was done as a strategy plugin.
    - Now all strategy plugins can inherit this behavior. The debugger defaults to activating when
    - a task is failed on unreachable. Use the debugger keyword for more flexibility.
  type: boolean
  env: [{name: ANSIBLE_ENABLE_TASK_DEBUGGER}]
  ini:
    - {key: enable_task_debugger, section: defaults}
  version_added: "2.5"
TASK_DEBUGGER_IGNORE_ERRORS:
  name: Whether a failed task with ignore_errors=True will still invoke the debugger
  default: True
  description:
    - This option defines whether the task debugger will be invoked on a failed task when ignore_errors=True
      is specified.
    - True specifies that the debugger will honor ignore_errors, False will not honor ignore_errors.
  type: boolean
  env: [{name: ANSIBLE_TASK_DEBUGGER_IGNORE_ERRORS}]
  ini:
    - {key: task_debugger_ignore_errors, section: defaults}
  version_added: "2.7"
DEFAULT_STRATEGY:
  name: Implied strategy
  default: 'linear'
  description: Set the default strategy used for plays.
  env: [{name: ANSIBLE_STRATEGY}]
  ini:
  - {key: strategy, section: defaults}
  version_added: "2.3"
DEFAULT_STRATEGY_PLUGIN_PATH:
  name: Strategy Plugins Path
  description: Colon separated paths in which Ansible will search for Strategy Plugins.
  default: ~/.ansible/plugins/strategy:/usr/share/ansible/plugins/strategy
  env: [{name: ANSIBLE_STRATEGY_PLUGINS}]
  ini:
  - {key: strategy_plugins, section: defaults}
  type: pathspec
DEFAULT_SU:
  default: False
  description: 'Toggle the use of "su" for tasks.'
  env: [{name: ANSIBLE_SU}]
  ini:
  - {key: su, section: defaults}
  type: boolean
  yaml: {key: defaults.su}
DEFAULT_SYSLOG_FACILITY:
  name: syslog facility
  default: LOG_USER
  description: Syslog facility to use when Ansible logs to the remote target
  env: [{name: ANSIBLE_SYSLOG_FACILITY}]
  ini:
  - {key: syslog_facility, section: defaults}
DEFAULT_TASK_INCLUDES_STATIC:
  name: Task include static
  default: False
  description:
    - The `include` tasks can be static or dynamic, this toggles the default expected behaviour if autodetection fails and it is not explicitly set in task.
  env: [{name: ANSIBLE_TASK_INCLUDES_STATIC}]
  ini:
  - {key: task_includes_static, section: defaults}
  type: boolean
  version_added: "2.1"
  deprecated:
    why: include itself is deprecated and this setting will not matter in the future
    version: "2.12"
    alternatives: None, as its already built into the decision between include_tasks and import_tasks
DEFAULT_TERMINAL_PLUGIN_PATH:
  name: Terminal Plugins Path
  default: ~/.ansible/plugins/terminal:/usr/share/ansible/plugins/terminal
  description: Colon separated paths in which Ansible will search for Terminal Plugins.
  env: [{name: ANSIBLE_TERMINAL_PLUGINS}]
  ini:
  - {key: terminal_plugins, section: defaults}
  type: pathspec
DEFAULT_TEST_PLUGIN_PATH:
  name: Jinja2 Test Plugins Path
  description: Colon separated paths in which Ansible will search for Jinja2 Test Plugins.
  default: ~/.ansible/plugins/test:/usr/share/ansible/plugins/test
  env: [{name: ANSIBLE_TEST_PLUGINS}]
  ini:
  - {key: test_plugins, section: defaults}
  type: pathspec
DEFAULT_TIMEOUT:
  name: Connection timeout
  default: 10
  description: This is the default timeout for connection plugins to use.
  env: [{name: ANSIBLE_TIMEOUT}]
  ini:
  - {key: timeout, section: defaults}
  type: integer
DEFAULT_TRANSPORT:
  # note that ssh_utils refs this and needs to be updated if removed
  name: Connection plugin
  default: smart
  description: "Default connection plugin to use, the 'smart' option will toggle between 'ssh' and 'paramiko' depending on controller OS and ssh versions"
  env: [{name: ANSIBLE_TRANSPORT}]
  ini:
  - {key: transport, section: defaults}
DEFAULT_UNDEFINED_VAR_BEHAVIOR:
  name: Jinja2 fail on undefined
  default: True
  version_added: "1.3"
  description:
    - When True, this causes ansible templating to fail steps that reference variable names that are likely typoed.
    - "Otherwise, any '{{ template_expression }}' that contains undefined variables will be rendered in a template or ansible action line exactly as written."
  env: [{name: ANSIBLE_ERROR_ON_UNDEFINED_VARS}]
  ini:
  - {key: error_on_undefined_vars, section: defaults}
  type: boolean
DEFAULT_VARS_PLUGIN_PATH:
  name: Vars Plugins Path
  default: ~/.ansible/plugins/vars:/usr/share/ansible/plugins/vars
  description: Colon separated paths in which Ansible will search for Vars Plugins.
  env: [{name: ANSIBLE_VARS_PLUGINS}]
  ini:
  - {key: vars_plugins, section: defaults}
  type: pathspec
# TODO: unused?
#DEFAULT_VAR_COMPRESSION_LEVEL:
#  default: 0
#  description: 'TODO: write it'
#  env: [{name: ANSIBLE_VAR_COMPRESSION_LEVEL}]
#  ini:
#  - {key: var_compression_level, section: defaults}
#  type: integer
#  yaml: {key: defaults.var_compression_level}
DEFAULT_VAULT_ID_MATCH:
  name: Force vault id match
  default: False
  description: 'If true, decrypting vaults with a vault id will only try the password from the matching vault-id'
  env: [{name: ANSIBLE_VAULT_ID_MATCH}]
  ini:
  - {key: vault_id_match, section: defaults}
  yaml: {key: defaults.vault_id_match}
DEFAULT_VAULT_IDENTITY:
  name: Vault id label
  default: default
  description: 'The label to use for the default vault id label in cases where a vault id label is not provided'
  env: [{name: ANSIBLE_VAULT_IDENTITY}]
  ini:
  - {key: vault_identity, section: defaults}
  yaml: {key: defaults.vault_identity}
DEFAULT_VAULT_ENCRYPT_IDENTITY:
  name: Vault id to use for encryption
  default:
  description: 'The vault_id to use for encrypting by default. If multiple vault_ids are provided, this specifies which to use for encryption. The --encrypt-vault-id cli option overrides the configured value.'
  env: [{name: ANSIBLE_VAULT_ENCRYPT_IDENTITY}]
  ini:
  - {key: vault_encrypt_identity, section: defaults}
  yaml: {key: defaults.vault_encrypt_identity}
DEFAULT_VAULT_IDENTITY_LIST:
  name: Default vault ids
  default: []
  description: 'A list of vault-ids to use by default. Equivalent to multiple --vault-id args. Vault-ids are tried in order.'
  env: [{name: ANSIBLE_VAULT_IDENTITY_LIST}]
  ini:
  - {key: vault_identity_list, section: defaults}
  type: list
  yaml: {key: defaults.vault_identity_list}
DEFAULT_VAULT_PASSWORD_FILE:
  name: Vault password file
  default: ~
  description: 'The vault password file to use. Equivalent to --vault-password-file or --vault-id'
  env: [{name: ANSIBLE_VAULT_PASSWORD_FILE}]
  ini:
  - {key: vault_password_file, section: defaults}
  type: path
  yaml: {key: defaults.vault_password_file}
DEFAULT_VERBOSITY:
  name: Verbosity
  default: 0
  description: Sets the default verbosity, equivalent to the number of ``-v`` passed in the command line.
  env: [{name: ANSIBLE_VERBOSITY}]
  ini:
  - {key: verbosity, section: defaults}
  type: integer
DEPRECATION_WARNINGS:
  name: Deprecation messages
  default: True
  description: "Toggle to control the showing of deprecation warnings"
  env: [{name: ANSIBLE_DEPRECATION_WARNINGS}]
  ini:
  - {key: deprecation_warnings, section: defaults}
  type: boolean
DEVEL_WARNING:
  name: Running devel warning
  default: True
  description: Toggle to control showing warnings related to running devel
  env: [{name: ANSIBLE_DEVEL_WARNING}]
  ini:
  - {key: devel_warning, section: defaults}
  type: boolean
DIFF_ALWAYS:
  name: Show differences
  default: False
  description: Configuration toggle to tell modules to show differences when in 'changed' status, equivalent to ``--diff``.
  env: [{name: ANSIBLE_DIFF_ALWAYS}]
  ini:
  - {key: always, section: diff}
  type: bool
DIFF_CONTEXT:
  name: Difference context
  default: 3
  description: How many lines of context to show when displaying the differences between files.
  env: [{name: ANSIBLE_DIFF_CONTEXT}]
  ini:
  - {key: context, section: diff}
  type: integer
DISPLAY_ARGS_TO_STDOUT:
  name: Show task arguments
  default: False
  description:
    - "Normally ``ansible-playbook`` will print a header for each task that is run.
      These headers will contain the name: field from the task if you specified one.
      If you didn't then ``ansible-playbook`` uses the task's action to help you tell which task is presently running.
      Sometimes you run many of the same action and so you want more information about the task to differentiate it from others of the same action.
      If you set this variable to True in the config then ``ansible-playbook`` will also include the task's arguments in the header."
    - "This setting defaults to False because there is a chance that you have sensitive values in your parameters and
      you do not want those to be printed."
    - "If you set this to True you should be sure that you have secured your environment's stdout
      (no one can shoulder surf your screen and you aren't saving stdout to an insecure file) or
      made sure that all of your playbooks explicitly added the ``no_log: True`` parameter to tasks which have sensitive values
      See How do I keep secret data in my playbook? for more information."
  env: [{name: ANSIBLE_DISPLAY_ARGS_TO_STDOUT}]
  ini:
  - {key: display_args_to_stdout, section: defaults}
  type: boolean
  version_added: "2.1"
DISPLAY_SKIPPED_HOSTS:
  name: Show skipped results
  default: True
  description: "Toggle to control displaying skipped task/host entries in a task in the default callback"
  env:
  - name: DISPLAY_SKIPPED_HOSTS
    deprecated:
      why: environment variables without ``ANSIBLE_`` prefix are deprecated
      version: "2.12"
      alternatives: the ``ANSIBLE_DISPLAY_SKIPPED_HOSTS`` environment variable
  - name: ANSIBLE_DISPLAY_SKIPPED_HOSTS
  ini:
  - {key: display_skipped_hosts, section: defaults}
  type: boolean
DOCSITE_ROOT_URL:
  name: Root docsite URL
  default: https://docs.ansible.com/ansible/
  description: Root docsite URL used to generate docs URLs in warning/error text;
               must be an absolute URL with valid scheme and trailing slash.
  ini:
  - {key: docsite_root_url, section: defaults}
  version_added: "2.8"
DUPLICATE_YAML_DICT_KEY:
  name: Controls ansible behaviour when finding duplicate keys in YAML.
  default: warn
  description:
    - By default Ansible will issue a warning when a duplicate dict key is encountered in YAML.
    - These warnings can be silenced by adjusting this setting to False.
  env: [{name: ANSIBLE_DUPLICATE_YAML_DICT_KEY}]
  ini:
  - {key: duplicate_dict_key, section: defaults}
  type: string
  choices: ['warn', 'error', 'ignore']
  version_added: "2.9"
ERROR_ON_MISSING_HANDLER:
  name: Missing handler error
  default: True
  description: "Toggle to allow missing handlers to become a warning instead of an error when notifying."
  env: [{name: ANSIBLE_ERROR_ON_MISSING_HANDLER}]
  ini:
  - {key: error_on_missing_handler, section: defaults}
  type: boolean
CONNECTION_FACTS_MODULES:
  name: Map of connections to fact modules
  default:
    # use ansible.legacy names on unqualified facts modules to allow library/ overrides
    asa: ansible.legacy.asa_facts
    cisco.asa.asa: cisco.asa.asa_facts
    eos: ansible.legacy.eos_facts
    arista.eos.eos: arista.eos.eos_facts
    frr: ansible.legacy.frr_facts
    frr.frr.frr: frr.frr.frr_facts
    ios: ansible.legacy.ios_facts
    cisco.ios.ios: cisco.ios.ios_facts
    iosxr: ansible.legacy.iosxr_facts
    cisco.iosxr.iosxr: cisco.iosxr.iosxr_facts
    junos: ansible.legacy.junos_facts
    junipernetworks.junos.junos: junipernetworks.junos.junos_facts
    nxos: ansible.legacy.nxos_facts
    cisco.nxos.nxos: cisco.nxos.nxos_facts
    vyos: ansible.legacy.vyos_facts
    vyos.vyos.vyos: vyos.vyos.vyos_facts
    exos: ansible.legacy.exos_facts
    extreme.exos.exos: extreme.exos.exos_facts
    slxos: ansible.legacy.slxos_facts
    extreme.slxos.slxos: extreme.slxos.slxos_facts
    voss: ansible.legacy.voss_facts
    extreme.voss.voss: extreme.voss.voss_facts
    ironware: ansible.legacy.ironware_facts
    community.network.ironware: community.network.ironware_facts
  description: "Which modules to run during a play's fact gathering stage based on connection"
  env: [{name: ANSIBLE_CONNECTION_FACTS_MODULES}]
  ini:
    - {key: connection_facts_modules, section: defaults}
  type: dict
FACTS_MODULES:
  name: Gather Facts Modules
  default:
    - smart
  description: "Which modules to run during a play's fact gathering stage, using the default of 'smart' will try to figure it out based on connection type."
  env: [{name: ANSIBLE_FACTS_MODULES}]
  ini:
    - {key: facts_modules, section: defaults}
  type: list
  vars:
    - name: ansible_facts_modules
GALAXY_IGNORE_CERTS:
  name: Galaxy validate certs
  default: False
  description:
    - If set to yes, ansible-galaxy will not validate TLS certificates.
      This can be useful for testing against a server with a self-signed certificate.
  env: [{name: ANSIBLE_GALAXY_IGNORE}]
  ini:
  - {key: ignore_certs, section: galaxy}
  type: boolean
GALAXY_ROLE_SKELETON:
  name: Galaxy role or collection skeleton directory
  default:
  description: Role or collection skeleton directory to use as a template for the ``init`` action in ``ansible-galaxy``, same as ``--role-skeleton``.
  env: [{name: ANSIBLE_GALAXY_ROLE_SKELETON}]
  ini:
  - {key: role_skeleton, section: galaxy}
  type: path
GALAXY_ROLE_SKELETON_IGNORE:
  name: Galaxy skeleton ignore
  default: ["^.git$", "^.*/.git_keep$"]
  description: patterns of files to ignore inside a Galaxy role or collection skeleton directory
  env: [{name: ANSIBLE_GALAXY_ROLE_SKELETON_IGNORE}]
  ini:
  - {key: role_skeleton_ignore, section: galaxy}
  type: list
# TODO: unused?
#GALAXY_SCMS:
#  name: Galaxy SCMS
#  default: git, hg
#  description: Available galaxy source control management systems.
#  env: [{name: ANSIBLE_GALAXY_SCMS}]
#  ini:
#  - {key: scms, section: galaxy}
#  type: list
GALAXY_SERVER:
  default: https://galaxy.ansible.com
  description: "URL to prepend when roles don't specify the full URI, assume they are referencing this server as the source."
  env: [{name: ANSIBLE_GALAXY_SERVER}]
  ini:
  - {key: server, section: galaxy}
  yaml: {key: galaxy.server}
GALAXY_SERVER_LIST:
  description:
  - A list of Galaxy servers to use when installing a collection.
  - The value corresponds to the config ini header ``[galaxy_server.{{item}}]`` which defines the server details.
  - 'See :ref:`galaxy_server_config` for more details on how to define a Galaxy server.'
  - The order of servers in this list is used to as the order in which a collection is resolved.
  - Setting this config option will ignore the :ref:`galaxy_server` config option.
  env: [{name: ANSIBLE_GALAXY_SERVER_LIST}]
  ini:
  - {key: server_list, section: galaxy}
  type: list
  version_added: "2.9"
GALAXY_TOKEN_PATH:
  default: ~/.ansible/galaxy_token
  description: "Local path to galaxy access token file"
  env: [{name: ANSIBLE_GALAXY_TOKEN_PATH}]
  ini:
  - {key: token_path, section: galaxy}
  type: path
  version_added: "2.9"
GALAXY_DISPLAY_PROGRESS:
  default: ~
  description:
  - Some steps in ``ansible-galaxy`` display a progress wheel which can cause issues on certain displays or when
    outputing the stdout to a file.
  - This config option controls whether the display wheel is shown or not.
  - The default is to show the display wheel if stdout has a tty.
  env: [{name: ANSIBLE_GALAXY_DISPLAY_PROGRESS}]
  ini:
  - {key: display_progress, section: galaxy}
  type: bool
  version_added: "2.10"
GALAXY_CACHE_DIR:
  default: ~/.ansible/galaxy_cache
  description:
  - The directory that stores cached responses from a Galaxy server.
  - This is only used by the ``ansible-galaxy collection install`` and ``download`` commands.
  - Cache files inside this dir will be ignored if they are world writable.
  env:
  - name: ANSIBLE_GALAXY_CACHE_DIR
  ini:
  - section: galaxy
    key: cache_dir
  type: path
  version_added: '2.11'
HOST_KEY_CHECKING:
  name: Check host keys
  default: True
  description: 'Set this to "False" if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host'
  env: [{name: ANSIBLE_HOST_KEY_CHECKING}]
  ini:
  - {key: host_key_checking, section: defaults}
  type: boolean
HOST_PATTERN_MISMATCH:
  name: Control host pattern mismatch behaviour
  default: 'warning'
  description: This setting changes the behaviour of mismatched host patterns, it allows you to force a fatal error, a warning or just ignore it
  env: [{name: ANSIBLE_HOST_PATTERN_MISMATCH}]
  ini:
  - {key: host_pattern_mismatch, section: inventory}
  choices: ['warning', 'error', 'ignore']
  version_added: "2.8"
INTERPRETER_PYTHON:
  name: Python interpreter path (or automatic discovery behavior) used for module execution
  default: auto_legacy
  env: [{name: ANSIBLE_PYTHON_INTERPRETER}]
  ini:
  - {key: interpreter_python, section: defaults}
  vars:
  - {name: ansible_python_interpreter}
  version_added: "2.8"
  description:
  - Path to the Python interpreter to be used for module execution on remote targets, or an automatic discovery mode.
    Supported discovery modes are ``auto``, ``auto_silent``, and ``auto_legacy`` (the default). All discovery modes
    employ a lookup table to use the included system Python (on distributions known to include one), falling back to a
    fixed ordered list of well-known Python interpreter locations if a platform-specific default is not available. The
    fallback behavior will issue a warning that the interpreter should be set explicitly (since interpreters installed
    later may change which one is used). This warning behavior can be disabled by setting ``auto_silent``. The default
    value of ``auto_legacy`` provides all the same behavior, but for backwards-compatibility with older Ansible releases
    that always defaulted to ``/usr/bin/python``, will use that interpreter if present (and issue a warning that the
    default behavior will change to that of ``auto`` in a future Ansible release.
INTERPRETER_PYTHON_DISTRO_MAP:
  name: Mapping of known included platform pythons for various Linux distros
  default:
    centos: &rhelish
      '6': /usr/bin/python
      '8': /usr/libexec/platform-python
    debian:
      '10': /usr/bin/python3
    fedora:
      '23': /usr/bin/python3
    redhat: *rhelish
    rhel: *rhelish
    ubuntu:
      '14': /usr/bin/python
      '16': /usr/bin/python3
  version_added: "2.8"
  # FUTURE: add inventory override once we're sure it can't be abused by a rogue target
  # FUTURE: add a platform layer to the map so we could use for, eg, freebsd/macos/etc?
INTERPRETER_PYTHON_FALLBACK:
  name: Ordered list of Python interpreters to check for in discovery
  default:
  - /usr/bin/python
  - python3.7
  - python3.6
  - python3.5
  - python2.7
  - python2.6
  - /usr/libexec/platform-python
  - /usr/bin/python3
  - python
  # FUTURE: add inventory override once we're sure it can't be abused by a rogue target
  version_added: "2.8"
TRANSFORM_INVALID_GROUP_CHARS:
  name: Transform invalid characters in group names
  default: 'never'
  description:
    - Make ansible transform invalid characters in group names supplied by inventory sources.
    - If 'never' it will allow for the group name but warn about the issue.
    - When 'ignore', it does the same as 'never', without issuing a warning.
    - When 'always' it will replace any invalid characters with '_' (underscore) and warn the user
    - When 'silently', it does the same as 'always', without issuing a warning.
  env: [{name: ANSIBLE_TRANSFORM_INVALID_GROUP_CHARS}]
  ini:
  - {key: force_valid_group_names, section: defaults}
  type: string
  choices: ['always', 'never', 'ignore', 'silently']
  version_added: '2.8'
INVALID_TASK_ATTRIBUTE_FAILED:
  name: Controls whether invalid attributes for a task result in errors instead of warnings
  default: True
  description: If 'false', invalid attributes for a task will result in warnings instead of errors
  type: boolean
  env:
    - name: ANSIBLE_INVALID_TASK_ATTRIBUTE_FAILED
  ini:
    - key: invalid_task_attribute_failed
      section: defaults
  version_added: "2.7"
INVENTORY_ANY_UNPARSED_IS_FAILED:
  name: Controls whether any unparseable inventory source is a fatal error
  default: False
  description: >
    If 'true', it is a fatal error when any given inventory source
    cannot be successfully parsed by any available inventory plugin;
    otherwise, this situation only attracts a warning.
  type: boolean
  env: [{name: ANSIBLE_INVENTORY_ANY_UNPARSED_IS_FAILED}]
  ini:
    - {key: any_unparsed_is_failed, section: inventory}
  version_added: "2.7"
INVENTORY_CACHE_ENABLED:
  name: Inventory caching enabled
  default: False
  description: Toggle to turn on inventory caching
  env: [{name: ANSIBLE_INVENTORY_CACHE}]
  ini:
  - {key: cache, section: inventory}
  type: bool
INVENTORY_CACHE_PLUGIN:
  name: Inventory cache plugin
  description: The plugin for caching inventory. If INVENTORY_CACHE_PLUGIN is not provided CACHE_PLUGIN can be used instead.
  env: [{name: ANSIBLE_INVENTORY_CACHE_PLUGIN}]
  ini:
  - {key: cache_plugin, section: inventory}
INVENTORY_CACHE_PLUGIN_CONNECTION:
  name: Inventory cache plugin URI to override the defaults section
  description: The inventory cache connection. If INVENTORY_CACHE_PLUGIN_CONNECTION is not provided CACHE_PLUGIN_CONNECTION can be used instead.
  env: [{name: ANSIBLE_INVENTORY_CACHE_CONNECTION}]
  ini:
  - {key: cache_connection, section: inventory}
INVENTORY_CACHE_PLUGIN_PREFIX:
  name: Inventory cache plugin table prefix
  description: The table prefix for the cache plugin. If INVENTORY_CACHE_PLUGIN_PREFIX is not provided CACHE_PLUGIN_PREFIX can be used instead.
  env: [{name: ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX}]
  default: ansible_facts
  ini:
  - {key: cache_prefix, section: inventory}
INVENTORY_CACHE_TIMEOUT:
  name: Inventory cache plugin expiration timeout
  description: Expiration timeout for the inventory cache plugin data. If INVENTORY_CACHE_TIMEOUT is not provided CACHE_TIMEOUT can be used instead.
  default: 3600
  env: [{name: ANSIBLE_INVENTORY_CACHE_TIMEOUT}]
  ini:
  - {key: cache_timeout, section: inventory}
INVENTORY_ENABLED:
  name: Active Inventory plugins
  default: ['host_list', 'script', 'auto', 'yaml', 'ini', 'toml']
  description: List of enabled inventory plugins, it also determines the order in which they are used.
  env: [{name: ANSIBLE_INVENTORY_ENABLED}]
  ini:
  - {key: enable_plugins, section: inventory}
  type: list
INVENTORY_EXPORT:
  name: Set ansible-inventory into export mode
  default: False
  description: Controls if ansible-inventory will accurately reflect Ansible's view into inventory or its optimized for exporting.
  env: [{name: ANSIBLE_INVENTORY_EXPORT}]
  ini:
  - {key: export, section: inventory}
  type: bool
INVENTORY_IGNORE_EXTS:
  name: Inventory ignore extensions
  default: "{{(REJECT_EXTS + ('.orig', '.ini', '.cfg', '.retry'))}}"
  description: List of extensions to ignore when using a directory as an inventory source
  env: [{name: ANSIBLE_INVENTORY_IGNORE}]
  ini:
  - {key: inventory_ignore_extensions, section: defaults}
  - {key: ignore_extensions, section: inventory}
  type: list
INVENTORY_IGNORE_PATTERNS:
  name: Inventory ignore patterns
  default: []
  description: List of patterns to ignore when using a directory as an inventory source
  env: [{name: ANSIBLE_INVENTORY_IGNORE_REGEX}]
  ini:
  - {key: inventory_ignore_patterns, section: defaults}
  - {key: ignore_patterns, section: inventory}
  type: list
INVENTORY_UNPARSED_IS_FAILED:
  name: Unparsed Inventory failure
  default: False
  description: >
    If 'true' it is a fatal error if every single potential inventory
    source fails to parse, otherwise this situation will only attract a
    warning.
  env: [{name: ANSIBLE_INVENTORY_UNPARSED_FAILED}]
  ini:
  - {key: unparsed_is_failed, section: inventory}
  type: bool
MAX_FILE_SIZE_FOR_DIFF:
  name: Diff maximum file size
  default: 104448
  description: Maximum size of files to be considered for diff display
  env: [{name: ANSIBLE_MAX_DIFF_SIZE}]
  ini:
  - {key: max_diff_size, section: defaults}
  type: int
NETWORK_GROUP_MODULES:
  name: Network module families
  default: [eos, nxos, ios, iosxr, junos, enos, ce, vyos, sros, dellos9, dellos10, dellos6, asa, aruba, aireos, bigip, ironware, onyx, netconf, exos, voss, slxos]
  description: 'TODO: write it'
  env:
  - name: NETWORK_GROUP_MODULES
    deprecated:
      why: environment variables without ``ANSIBLE_`` prefix are deprecated
      version: "2.12"
      alternatives: the ``ANSIBLE_NETWORK_GROUP_MODULES`` environment variable
  - name: ANSIBLE_NETWORK_GROUP_MODULES
  ini:
  - {key: network_group_modules, section: defaults}
  type: list
  yaml: {key: defaults.network_group_modules}
INJECT_FACTS_AS_VARS:
  default: True
  description:
    - Facts are available inside the `ansible_facts` variable, this setting also pushes them as their own vars in the main namespace.
    - Unlike inside the `ansible_facts` dictionary, these will have an `ansible_` prefix.
  env: [{name: ANSIBLE_INJECT_FACT_VARS}]
  ini:
  - {key: inject_facts_as_vars, section: defaults}
  type: boolean
  version_added: "2.5"
MODULE_IGNORE_EXTS:
  name: Module ignore extensions
  default: "{{(REJECT_EXTS + ('.yaml', '.yml', '.ini'))}}"
  description:
    - List of extensions to ignore when looking for modules to load
    - This is for rejecting script and binary module fallback extensions
  env: [{name: ANSIBLE_MODULE_IGNORE_EXTS}]
  ini:
  - {key: module_ignore_exts, section: defaults}
  type: list
OLD_PLUGIN_CACHE_CLEARING:
  description: Previouslly Ansible would only clear some of the plugin loading caches when loading new roles, this led to some behaviours in which a plugin loaded in prevoius plays would be unexpectedly 'sticky'. This setting allows to return to that behaviour.
  env: [{name: ANSIBLE_OLD_PLUGIN_CACHE_CLEAR}]
  ini:
  - {key: old_plugin_cache_clear, section: defaults}
  type: boolean
  default: False
  version_added: "2.8"
PARAMIKO_HOST_KEY_AUTO_ADD:
  # TODO: move to plugin
  default: False
  description: 'TODO: write it'
  env: [{name: ANSIBLE_PARAMIKO_HOST_KEY_AUTO_ADD}]
  ini:
  - {key: host_key_auto_add, section: paramiko_connection}
  type: boolean
PARAMIKO_LOOK_FOR_KEYS:
  name: look for keys
  default: True
  description: 'TODO: write it'
  env: [{name: ANSIBLE_PARAMIKO_LOOK_FOR_KEYS}]
  ini:
  - {key: look_for_keys, section: paramiko_connection}
  type: boolean
PERSISTENT_CONTROL_PATH_DIR:
  name: Persistence socket path
  default: ~/.ansible/pc
  description: Path to socket to be used by the connection persistence system.
  env: [{name: ANSIBLE_PERSISTENT_CONTROL_PATH_DIR}]
  ini:
  - {key: control_path_dir, section: persistent_connection}
  type: path
PERSISTENT_CONNECT_TIMEOUT:
  name: Persistence timeout
  default: 30
  description: This controls how long the persistent connection will remain idle before it is destroyed.
  env: [{name: ANSIBLE_PERSISTENT_CONNECT_TIMEOUT}]
  ini:
  - {key: connect_timeout, section: persistent_connection}
  type: integer
PERSISTENT_CONNECT_RETRY_TIMEOUT:
  name: Persistence connection retry timeout
  default: 15
  description: This controls the retry timeout for persistent connection to connect to the local domain socket.
  env: [{name: ANSIBLE_PERSISTENT_CONNECT_RETRY_TIMEOUT}]
  ini:
  - {key: connect_retry_timeout, section: persistent_connection}
  type: integer
PERSISTENT_COMMAND_TIMEOUT:
  name: Persistence command timeout
  default: 30
  description: This controls the amount of time to wait for response from remote device before timing out persistent connection.
  env: [{name: ANSIBLE_PERSISTENT_COMMAND_TIMEOUT}]
  ini:
  - {key: command_timeout, section: persistent_connection}
  type: int
PLAYBOOK_DIR:
  name: playbook dir override for non-playbook CLIs (ala --playbook-dir)
  version_added: "2.9"
  description:
    - A number of non-playbook CLIs have a ``--playbook-dir`` argument; this sets the default value for it.
  env: [{name: ANSIBLE_PLAYBOOK_DIR}]
  ini: [{key: playbook_dir, section: defaults}]
  type: path
PLAYBOOK_VARS_ROOT:
  name: playbook vars files root
  default: top
  version_added: "2.4.1"
  description:
    - This sets which playbook dirs will be used as a root to process vars plugins, which includes finding host_vars/group_vars
    - The ``top`` option follows the traditional behaviour of using the top playbook in the chain to find the root directory.
    - The ``bottom`` option follows the 2.4.0 behaviour of using the current playbook to find the root directory.
    - The ``all`` option examines from the first parent to the current playbook.
  env: [{name: ANSIBLE_PLAYBOOK_VARS_ROOT}]
  ini:
  - {key: playbook_vars_root, section: defaults}
  choices: [ top, bottom, all ]
PLUGIN_FILTERS_CFG:
  name: Config file for limiting valid plugins
  default: null
  version_added: "2.5.0"
  description:
    - "A path to configuration for filtering which plugins installed on the system are allowed to be used."
    - "See :ref:`plugin_filtering_config` for details of the filter file's format."
    - " The default is /etc/ansible/plugin_filters.yml"
  ini:
  - key: plugin_filters_cfg
    section: default
    deprecated:
      why: specifying "plugin_filters_cfg" under the "default" section is deprecated
      version: "2.12"
      alternatives: the "defaults" section instead
  - key: plugin_filters_cfg
    section: defaults
  type: path
PYTHON_MODULE_RLIMIT_NOFILE:
  name: Adjust maximum file descriptor soft limit during Python module execution
  description:
  - Attempts to set RLIMIT_NOFILE soft limit to the specified value when executing Python modules (can speed up subprocess usage on
    Python 2.x. See https://bugs.python.org/issue11284). The value will be limited by the existing hard limit. Default
    value of 0 does not attempt to adjust existing system-defined limits.
  default: 0
  env:
  - {name: ANSIBLE_PYTHON_MODULE_RLIMIT_NOFILE}
  ini:
  - {key: python_module_rlimit_nofile, section: defaults}
  vars:
  - {name: ansible_python_module_rlimit_nofile}
  version_added: '2.8'
RETRY_FILES_ENABLED:
  name: Retry files
  default: False
  description: This controls whether a failed Ansible playbook should create a .retry file.
  env: [{name: ANSIBLE_RETRY_FILES_ENABLED}]
  ini:
  - {key: retry_files_enabled, section: defaults}
  type: bool
RETRY_FILES_SAVE_PATH:
  name: Retry files path
  default: ~
  description:
    - This sets the path in which Ansible will save .retry files when a playbook fails and retry files are enabled.
    - This file will be overwritten after each run with the list of failed hosts from all plays.
  env: [{name: ANSIBLE_RETRY_FILES_SAVE_PATH}]
  ini:
  - {key: retry_files_save_path, section: defaults}
  type: path
RUN_VARS_PLUGINS:
  name: When should vars plugins run relative to inventory
  default: demand
  description:
    - This setting can be used to optimize vars_plugin usage depending on user's inventory size and play selection.
    - Setting to C(demand) will run vars_plugins relative to inventory sources anytime vars are 'demanded' by tasks.
    - Setting to C(start) will run vars_plugins relative to inventory sources after importing that inventory source.
  env: [{name: ANSIBLE_RUN_VARS_PLUGINS}]
  ini:
  - {key: run_vars_plugins, section: defaults}
  type: str
  choices: ['demand', 'start']
  version_added: "2.10"
SHOW_CUSTOM_STATS:
  name: Display custom stats
  default: False
  description: 'This adds the custom stats set via the set_stats plugin to the default output'
  env: [{name: ANSIBLE_SHOW_CUSTOM_STATS}]
  ini:
  - {key: show_custom_stats, section: defaults}
  type: bool
STRING_TYPE_FILTERS:
  name: Filters to preserve strings
  default: [string, to_json, to_nice_json, to_yaml, to_nice_yaml, ppretty, json]
  description:
    - "This list of filters avoids 'type conversion' when templating variables"
    - Useful when you want to avoid conversion into lists or dictionaries for JSON strings, for example.
  env: [{name: ANSIBLE_STRING_TYPE_FILTERS}]
  ini:
  - {key: dont_type_filters, section: jinja2}
  type: list
SYSTEM_WARNINGS:
  name: System warnings
  default: True
  description:
    - Allows disabling of warnings related to potential issues on the system running ansible itself (not on the managed hosts)
    - These may include warnings about 3rd party packages or other conditions that should be resolved if possible.
  env: [{name: ANSIBLE_SYSTEM_WARNINGS}]
  ini:
  - {key: system_warnings, section: defaults}
  type: boolean
TAGS_RUN:
  name: Run Tags
  default: []
  type: list
  description: default list of tags to run in your plays, Skip Tags has precedence.
  env: [{name: ANSIBLE_RUN_TAGS}]
  ini:
  - {key: run, section: tags}
  version_added: "2.5"
TAGS_SKIP:
  name: Skip Tags
  default: []
  type: list
  description: default list of tags to skip in your plays, has precedence over Run Tags
  env: [{name: ANSIBLE_SKIP_TAGS}]
  ini:
  - {key: skip, section: tags}
  version_added: "2.5"
TASK_TIMEOUT:
  name: Task Timeout
  default: 0
  description:
    - Set the maximum time (in seconds) that a task can run for.
    - If set to 0 (the default) there is no timeout.
  env: [{name: ANSIBLE_TASK_TIMEOUT}]
  ini:
  - {key: task_timeout, section: defaults}
  type: integer
  version_added: '2.10'
WORKER_SHUTDOWN_POLL_COUNT:
  name: Worker Shutdown Poll Count
  default: 0
  description:
    - The maximum number of times to check Task Queue Manager worker processes to verify they have exited cleanly.
    - After this limit is reached any worker processes still running will be terminated.
    - This is for internal use only.
  env: [{name: ANSIBLE_WORKER_SHUTDOWN_POLL_COUNT}]
  type: integer
  version_added: '2.10'
WORKER_SHUTDOWN_POLL_DELAY:
  name: Worker Shutdown Poll Delay
  default: 0.1
  description:
    - The number of seconds to sleep between polling loops when checking Task Queue Manager worker processes to verify they have exited cleanly.
    - This is for internal use only.
  env: [{name: ANSIBLE_WORKER_SHUTDOWN_POLL_DELAY}]
  type: float
  version_added: '2.10'
USE_PERSISTENT_CONNECTIONS:
  name: Persistence
  default: False
  description: Toggles the use of persistence for connections.
  env: [{name: ANSIBLE_USE_PERSISTENT_CONNECTIONS}]
  ini:
  - {key: use_persistent_connections, section: defaults}
  type: boolean
VARIABLE_PLUGINS_ENABLED:
  name: Vars plugin enabled list
  default: ['host_group_vars']
  description: Whitelist for variable plugins that require it.
  env: [{name: ANSIBLE_VARS_ENABLED}]
  ini:
  - {key: vars_plugins_enabled, section: defaults}
  type: list
  version_added: "2.10"
VARIABLE_PRECEDENCE:
  name: Group variable precedence
  default: ['all_inventory', 'groups_inventory', 'all_plugins_inventory', 'all_plugins_play', 'groups_plugins_inventory', 'groups_plugins_play']
  description: Allows to change the group variable precedence merge order.
  env: [{name: ANSIBLE_PRECEDENCE}]
  ini:
  - {key: precedence, section: defaults}
  type: list
  version_added: "2.4"
WIN_ASYNC_STARTUP_TIMEOUT:
  name: Windows Async Startup Timeout
  default: 5
  description:
    - For asynchronous tasks in Ansible (covered in Asynchronous Actions and Polling),
      this is how long, in seconds, to wait for the task spawned by Ansible to connect back to the named pipe used
      on Windows systems. The default is 5 seconds. This can be too low on slower systems, or systems under heavy load.
    - This is not the total time an async command can run for, but is a separate timeout to wait for an async command to
      start. The task will only start to be timed against its async_timeout once it has connected to the pipe, so the
      overall maximum duration the task can take will be extended by the amount specified here.
  env: [{name: ANSIBLE_WIN_ASYNC_STARTUP_TIMEOUT}]
  ini:
    - {key: win_async_startup_timeout, section: defaults}
  type: integer
  vars:
    - {name: ansible_win_async_startup_timeout}
  version_added: '2.10'
YAML_FILENAME_EXTENSIONS:
  name: Valid YAML extensions
  default: [".yml", ".yaml", ".json"]
  description:
    - "Check all of these extensions when looking for 'variable' files which should be YAML or JSON or vaulted versions of these."
    - 'This affects vars_files, include_vars, inventory and vars plugins among others.'
  env:
    - name: ANSIBLE_YAML_FILENAME_EXT
  ini:
    - section: defaults
      key: yaml_valid_extensions
  type: list
NETCONF_SSH_CONFIG:
  description: This variable is used to enable bastion/jump host with netconf connection. If set to True the bastion/jump
               host ssh settings should be present in ~/.ssh/config file, alternatively it can be set
               to custom ssh configuration file path to read the bastion/jump host settings.
  env: [{name: ANSIBLE_NETCONF_SSH_CONFIG}]
  ini:
  - {key: ssh_config, section: netconf_connection}
  yaml: {key: netconf_connection.ssh_config}
  default: null
STRING_CONVERSION_ACTION:
  version_added: '2.8'
  description:
    - Action to take when a module parameter value is converted to a string (this does not affect variables).
      For string parameters, values such as '1.00', "['a', 'b',]", and 'yes', 'y', etc.
      will be converted by the YAML parser unless fully quoted.
    - Valid options are 'error', 'warn', and 'ignore'.
    - Since 2.8, this option defaults to 'warn' but will change to 'error' in 2.12.
  default: 'warn'
  env:
    - name: ANSIBLE_STRING_CONVERSION_ACTION
  ini:
    - section: defaults
      key: string_conversion_action
  type: string
VERBOSE_TO_STDERR:
  version_added: '2.8'
  description:
    - Force 'verbose' option to use stderr instead of stdout
  default: False
  env:
    - name: ANSIBLE_VERBOSE_TO_STDERR
  ini:
    - section: defaults
      key: verbose_to_stderr
  type: bool
..."""