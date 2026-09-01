"""A Powerfull label editor"""


from plugin import InvenTreePlugin

from plugin.mixins import ReportMixin, ScheduleMixin, SettingsMixin, UserInterfaceMixin

from . import PLUGIN_VERSION


class InvertreeLabelEditor(ReportMixin, ScheduleMixin, SettingsMixin, UserInterfaceMixin, InvenTreePlugin):

    """InvertreeLabelEditor - custom InvenTree plugin."""

    # Plugin metadata
    TITLE = "Invertree Label Editor"
    NAME = "InvertreeLabelEditor"
    SLUG = "invertree-label-editor"
    DESCRIPTION = "A Powerfull label editor"
    VERSION = PLUGIN_VERSION

    # Additional project information
    AUTHOR = "manast"
    
    LICENSE = "MIT"

    # Optionally specify supported InvenTree versions
    # MIN_VERSION = '0.18.0'
    # MAX_VERSION = '2.0.0'

    # Render custom UI elements to the plugin settings page
    ADMIN_SOURCE = "Settings.js:RenderPluginSettings"
    
    # Scheduled tasks (from ScheduleMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/schedule/
    SCHEDULED_TASKS = {
        # Define your scheduled tasks here...
    }
    
    # Plugin settings (from SettingsMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/settings/
    SETTINGS = {
        # Define your plugin settings here...
        'CUSTOM_VALUE': {
            'name': 'Custom Value',
            'description': 'A custom value',
            'validator': int,
            'default': 42,
        }
    }
    
    
    
    
    # Custom report context (from ReportMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/report/
    def add_label_context(self, label_instance, model_instance, request, context, **kwargs):
        """Add custom context data to a label rendering context."""
        
        # Add custom context data to the label rendering context
        context['foo'] = 'label_bar'

    def add_report_context(self, report_instance, model_instance, request, context, **kwargs):
        """Add custom context data to a report rendering context."""
        
        # Add custom context data to the report rendering context
        context['foo'] = 'report_bar'

    def report_callback(self, template, instance, report, request, **kwargs):
        """Callback function called after a report is generated."""
        ...
    
    

    # User interface elements (from UserInterfaceMixin)
    # Ref: https://docs.inventree.org/en/latest/plugins/mixins/ui/
    
    # Custom UI panels
    def get_ui_panels(self, request, context: dict, **kwargs):
        """Return a list of custom panels to be rendered in the InvenTree user interface."""

        panels = []

        # Only display this panel for the 'part' target
        if context.get('target_model') == 'part':
            panels.append({
                'key': 'invertree-label-editor-panel',
                'title': 'Invertree Label Editor',
                'description': 'Custom panel description',
                'icon': 'ti:mood-smile:outline',
                'source': self.plugin_static_file('Panel.js:RenderInvertreeLabelEditorPanel'),
                'context': {
                    # Provide additional context data to the panel
                    'settings': self.get_settings_dict(),
                    'foo': 'bar'
                }
            })
        
        return panels
    

    # Custom dashboard items
    def get_ui_dashboard_items(self, request, context: dict, **kwargs):
        """Return a list of custom dashboard items to be rendered in the InvenTree user interface."""

        # Example: only display for 'staff' users
        if not request.user or not request.user.is_staff:
            return []
        
        items = []

        items.append({
            'key': 'invertree-label-editor-dashboard',
            'title': 'Invertree Label Editor Dashboard Item',
            'description': 'Custom dashboard item',
            'icon': 'ti:dashboard:outline',
            'source': self.plugin_static_file('Dashboard.js:RenderInvertreeLabelEditorDashboardItem'),
            'context': {
                # Provide additional context data to the dashboard item
                'settings': self.get_settings_dict(),
                'bar': 'foo'
            }
        })

        return items
    

    def get_ui_spotlight_actions(self, request, context, **kwargs):
        """Return a list of custom spotlight actions to be made available."""
        return [
            {
                'key': 'sample-spotlight-action',
                'title': 'Hello Action',
                'description': 'Hello from InvertreeLabelEditor',
                'icon': 'ti:heart-handshake:outline',
                'source': self.plugin_static_file(
                    'Spotlight.js:InvertreeLabelEditorSpotlightAction'
                ),
            }
        ]
    
